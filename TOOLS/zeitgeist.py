#!/usr/bin/env python3
"""
Monday Zeitgeist Scanner

Researches AI trends across 4 categories and adds ideas to the backlog.
Uses Claude CLI (already authenticated) instead of API directly.

Usage:
    python zeitgeist.py                    # Run research and update backlog
    python zeitgeist.py --dry-run          # Show what would be added without saving
    python zeitgeist.py --category social  # Only run one category
    python zeitgeist.py --create-tasks     # Also create Todoist tasks for the week
"""

import os
import sys
import yaml
import json
import argparse
import subprocess
import requests
from datetime import datetime, timedelta
from pathlib import Path

# Optional Todoist integration
try:
    from todoist_api_python.api import TodoistAPI
    TODOIST_AVAILABLE = True
except ImportError:
    TODOIST_AVAILABLE = False

# Configuration
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
BACKLOG_PATH = PROJECT_ROOT / "BACKLOG" / "ideas.yaml"
CONFIG_PATH = SCRIPT_DIR / "zeitgeist_config.yaml"

CATEGORIES = {
    "social": {
        "pillar": "enterprise",
        "prompt": """Research the latest AI trends being discussed on social media (Twitter/X, LinkedIn, Reddit, Hacker News) from the past week.

Focus on:
- Viral AI discussions or debates
- New tools getting attention
- Controversial takes or hot debates
- Memes or cultural moments around AI

Return 2-3 content ideas that would resonate with a technical audience. Each idea should have a contrarian or insightful angle, not just "here's what's trending."
"""
    },
    "tribal": {
        "pillar": "tribal",
        "prompt": """Research recent news and developments at the intersection of AI and Indigenous communities from the past week.

Focus on:
- AI sovereignty and data governance initiatives
- Tribal tech projects or announcements
- Indigenous perspectives on AI ethics
- Language preservation or cultural AI projects
- Any problematic AI deployments affecting Indigenous communities

Return 2-3 content ideas. Frame them from an Indigenous-led perspective, not a savior narrative.
"""
    },
    "enterprise": {
        "pillar": "enterprise",
        "prompt": """Research recent enterprise AI deployment news and case studies from the past week.

Focus on:
- Companies sharing production AI learnings
- Agent deployment case studies
- AI infrastructure and tooling announcements
- Failures or post-mortems (often more valuable than successes)
- Practical implementation patterns

Return 2-3 content ideas focused on "what actually works" rather than hype.
"""
    },
    "fun": {
        "pillar": "experiments",
        "prompt": """Research creative, weird, or playful AI projects from the past week.

Focus on:
- Unusual applications of AI
- Art, music, or creative projects
- Games and simulations using AI
- Visualizations and data art
- "What if?" experiments

Return 2-3 content ideas that are fun and demonstrate personality. These should make someone smile or think "that's clever."
"""
    }
}

IDEA_FORMAT = """
For each idea, provide:
1. title: A compelling title (action-oriented, specific)
2. hook: One sentence that makes someone want to read it
3. notes: Any relevant sources or context

Format as JSON array:
[
  {"title": "...", "hook": "...", "notes": "..."},
  ...
]

IMPORTANT: Return ONLY the JSON array, no other text.
"""


def load_config():
    """Load configuration from yaml file or environment."""
    config = {
        "ntfy_topic": os.environ.get("NTFY_TOPIC"),
        "ntfy_server": os.environ.get("NTFY_SERVER", "https://ntfy.sh"),
        "todoist_api_token": os.environ.get("TODOIST_API_TOKEN"),
        "todoist_project": os.environ.get("TODOIST_PROJECT", "Content Studio"),
    }

    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            file_config = yaml.safe_load(f) or {}
            config.update({k: v for k, v in file_config.items() if v})

    return config


def create_todoist_tasks(config, new_ideas):
    """Create Todoist tasks for the week's content."""
    if not TODOIST_AVAILABLE:
        print("  Todoist API not installed. Run: pip install todoist-api-python")
        return

    if not config.get('todoist_api_token'):
        print("  Skipping Todoist tasks (no todoist_api_token configured)")
        return

    try:
        api = TodoistAPI(config['todoist_api_token'])

        # Find or note the project (handle paginator)
        project_name = config.get('todoist_project', 'Content Studio')
        all_projects = []
        for page in api.get_projects():
            if isinstance(page, list):
                all_projects.extend(page)
            else:
                all_projects.append(page)
        project = next((p for p in all_projects if p.name == project_name), None)
        project_id = project.id if project else None

        if not project_id:
            print(f"  Note: Project '{project_name}' not found, tasks will go to Inbox")

        # Pick the most timely ideas (prioritize tribal and enterprise)
        priority_ideas = [i for i in new_ideas if i['pillar'] in ('tribal', 'enterprise')][:2]
        if len(priority_ideas) < 2:
            priority_ideas += [i for i in new_ideas if i not in priority_ideas][:2 - len(priority_ideas)]

        tasks_created = []

        # Create "Review zeitgeist ideas" task for today
        task = api.add_task(
            content="Review zeitgeist ideas and pick content for the week",
            description=f"Zeitgeist scan found {len(new_ideas)} new ideas. Review BACKLOG/ideas.yaml",
            due_string="today",
            project_id=project_id,
            priority=3  # p2 in Todoist (priority is inverted: 4=p1, 3=p2, 2=p3, 1=p4)
        )
        tasks_created.append(task.content)

        # Create LinkedIn post tasks for Tue/Thu
        if len(priority_ideas) >= 1:
            task = api.add_task(
                content=f"Write LinkedIn post: {priority_ideas[0]['title']}",
                description=priority_ideas[0]['hook'],
                due_string="tuesday 9am",
                project_id=project_id,
                priority=2
            )
            tasks_created.append(task.content)

        if len(priority_ideas) >= 2:
            task = api.add_task(
                content=f"Write LinkedIn post: {priority_ideas[1]['title']}",
                description=priority_ideas[1]['hook'],
                due_string="thursday 9am",
                project_id=project_id,
                priority=2
            )
            tasks_created.append(task.content)

        # Create flagship blog post task for Friday
        # Pick the meatiest enterprise or tribal idea
        flagship_candidates = [i for i in new_ideas if i['pillar'] in ('tribal', 'enterprise')]
        if flagship_candidates:
            flagship = flagship_candidates[0]
            task = api.add_task(
                content=f"Draft blog post: {flagship['title']}",
                description=f"{flagship['hook']}\n\nNotes: {flagship.get('notes', '')}",
                due_string="friday 2pm",
                project_id=project_id,
                priority=3
            )
            tasks_created.append(task.content)

        print(f"  Created {len(tasks_created)} Todoist tasks:")
        for t in tasks_created:
            print(f"    - {t}")

    except Exception as e:
        print(f"  Failed to create Todoist tasks: {e}")


def research_category(category_name: str, category_config: dict) -> list:
    """Use Claude CLI to research a category and generate ideas."""

    prompt = f"""{category_config['prompt']}

{IDEA_FORMAT}

Today's date: {datetime.now().strftime('%Y-%m-%d')}
"""

    print(f"  Researching {category_name}...")

    try:
        result = subprocess.run(
            [
                "claude", "-p", prompt,
                "--output-format", "text",
                "--permission-mode", "bypassPermissions",
                "--allowedTools", "WebSearch"
            ],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode != 0:
            print(f"    Error: {result.stderr}")
            return []

        text = result.stdout.strip()

        # Find JSON array in response
        start = text.find('[')
        end = text.rfind(']') + 1
        if start >= 0 and end > start:
            ideas_json = text[start:end]
            ideas = json.loads(ideas_json)

            # Add pillar and metadata to each idea
            for idea in ideas:
                idea['pillar'] = category_config['pillar']
                idea['status'] = 'seed'
                idea['added'] = datetime.now().strftime('%Y-%m-%d')
                idea['source'] = f"zeitgeist-{datetime.now().strftime('%Y-%m-%d')}"

            return ideas
        else:
            print(f"    Warning: Could not parse ideas from response")
            print(f"    Response: {text[:200]}...")
            return []

    except subprocess.TimeoutExpired:
        print(f"    Timeout researching {category_name}")
        return []
    except Exception as e:
        print(f"    Error researching {category_name}: {e}")
        return []


def load_backlog():
    """Load existing backlog."""
    if BACKLOG_PATH.exists():
        with open(BACKLOG_PATH) as f:
            data = yaml.safe_load(f)
            return data.get('ideas', []) if data else []
    return []


def save_backlog(ideas):
    """Save ideas to backlog."""
    BACKLOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    content = """# Content Ideas Backlog
# Status: seed | researching | drafting | review | published | archived
# Pillar: enterprise | tribal | deep-dive | experiments

ideas:
"""

    for idea in ideas:
        # Escape quotes in strings
        title = idea.get('title', '').replace('"', '\\"')
        hook = idea.get('hook', '').replace('"', '\\"')
        notes = idea.get('notes', '').replace('"', '\\"')

        content += f"""  - title: "{title}"
    pillar: {idea.get('pillar', 'enterprise')}
    status: {idea.get('status', 'seed')}
    hook: "{hook}"
    notes: "{notes}"
    added: {idea.get('added', datetime.now().strftime('%Y-%m-%d'))}
"""
        if idea.get('source'):
            content += f"    source: {idea['source']}\n"
        content += "\n"

    with open(BACKLOG_PATH, 'w') as f:
        f.write(content)


def send_notification(config, new_ideas):
    """Send ntfy notification with summary."""
    if not config.get('ntfy_topic'):
        print("  Skipping notification (no ntfy_topic configured)")
        return

    count = len(new_ideas)
    titles = [idea['title'] for idea in new_ideas[:5]]

    message = f"Added {count} ideas to backlog:\n" + "\n".join(f"- {t}" for t in titles)
    if count > 5:
        message += f"\n...and {count - 5} more"

    try:
        url = f"{config['ntfy_server']}/{config['ntfy_topic']}"
        requests.post(url, data=message.encode('utf-8'), headers={
            "Title": f"Zeitgeist: {count} new ideas",
            "Tags": "bulb,robot"
        })
        print(f"  Notification sent to {config['ntfy_topic']}")
    except Exception as e:
        print(f"  Failed to send notification: {e}")


def main():
    parser = argparse.ArgumentParser(description="Monday Zeitgeist Scanner")
    parser.add_argument("--dry-run", action="store_true", help="Show ideas without saving")
    parser.add_argument("--category", choices=list(CATEGORIES.keys()), help="Only run one category")
    parser.add_argument("--no-notify", action="store_true", help="Skip ntfy notification")
    parser.add_argument("--create-tasks", action="store_true", help="Create Todoist tasks for the week")
    args = parser.parse_args()

    print("=== Zeitgeist Scanner ===")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    # Check claude CLI is available
    try:
        subprocess.run(["claude", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: claude CLI not found or not working")
        print("Install: npm install -g @anthropic-ai/claude-code")
        sys.exit(1)

    config = load_config()

    # Determine which categories to run
    categories_to_run = {args.category: CATEGORIES[args.category]} if args.category else CATEGORIES

    # Research each category
    new_ideas = []
    for name, cat_config in categories_to_run.items():
        ideas = research_category(name, cat_config)
        new_ideas.extend(ideas)
        print(f"    Found {len(ideas)} ideas")

    print()
    print(f"Total new ideas: {len(new_ideas)}")

    # Display ideas
    for idea in new_ideas:
        print(f"\n  [{idea['pillar']}] {idea['title']}")
        print(f"    {idea['hook']}")

    if args.dry_run:
        print("\n--dry-run: Not saving to backlog")
        return

    # Load existing and merge
    existing = load_backlog()
    all_ideas = existing + new_ideas

    # Save
    save_backlog(all_ideas)
    print(f"\nSaved {len(new_ideas)} new ideas to {BACKLOG_PATH}")

    # Notify
    if not args.no_notify and new_ideas:
        send_notification(config, new_ideas)

    # Create Todoist tasks
    if args.create_tasks and new_ideas:
        create_todoist_tasks(config, new_ideas)

    print("\nDone!")


if __name__ == "__main__":
    main()
