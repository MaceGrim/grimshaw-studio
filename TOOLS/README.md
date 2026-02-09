# Grimshaw Studio Tools

## Zeitgeist Scanner

Automated weekly research of AI trends across 4 categories:
- **Social**: Viral discussions, debates, cultural moments
- **Tribal**: Indigenous AI, sovereignty, tribal tech
- **Enterprise**: Production deployments, case studies
- **Fun**: Creative projects, experiments, inspiration

### Setup

1. Install dependencies:
   ```bash
   pip install anthropic requests pyyaml
   ```

2. Configure API key (choose one):
   ```bash
   # Option A: Environment variable
   export ANTHROPIC_API_KEY=sk-ant-...

   # Option B: Config file
   cp zeitgeist_config.yaml zeitgeist_config.local.yaml
   # Edit zeitgeist_config.local.yaml with your key
   ```

3. (Optional) Configure ntfy for notifications:
   ```bash
   export NTFY_TOPIC=your-topic-name
   ```

### Usage

```bash
# Run full scan
python zeitgeist.py

# Dry run (show ideas without saving)
python zeitgeist.py --dry-run

# Run single category
python zeitgeist.py --category tribal

# Skip notification
python zeitgeist.py --no-notify

# Also create Todoist tasks for the week
python zeitgeist.py --create-tasks
```

### Todoist Integration

The `--create-tasks` flag creates weekly content tasks directly via the Todoist API (bypasses the MCP server which can timeout).

1. Get your API token: https://todoist.com/app/settings/integrations/developer

2. Configure (choose one):
   ```bash
   # Option A: Environment variable
   export TODOIST_API_TOKEN=your-token-here

   # Option B: Config file
   # Add to zeitgeist_config.yaml:
   # todoist_api_token: your-token-here
   ```

3. (Optional) Create a "Content Studio" project in Todoist, or set a different project:
   ```bash
   export TODOIST_PROJECT="My Content Project"
   ```

Tasks created each week:
- **Monday**: "Review zeitgeist ideas and pick content for the week"
- **Tuesday 9am**: LinkedIn post about top tribal/enterprise idea
- **Thursday 9am**: LinkedIn post about second idea
- **Friday 2pm**: Draft flagship blog post

### Cron Setup

Add to crontab to run every Monday at 8 AM:

```bash
# Edit crontab
crontab -e

# Add this line (adjust paths as needed)
0 8 * * 1 cd /mnt/o/Mason/Github/grimshaw-studio/TOOLS && /usr/bin/python3 zeitgeist.py >> /tmp/zeitgeist.log 2>&1
```

Or using systemd timer for more reliability:

```bash
# ~/.config/systemd/user/zeitgeist.service
[Unit]
Description=Zeitgeist Scanner

[Service]
Type=oneshot
WorkingDirectory=/mnt/o/Mason/Github/grimshaw-studio/TOOLS
ExecStart=/usr/bin/python3 zeitgeist.py
Environment=ANTHROPIC_API_KEY=sk-ant-...
Environment=NTFY_TOPIC=grimshaw-studio

# ~/.config/systemd/user/zeitgeist.timer
[Unit]
Description=Run Zeitgeist Scanner weekly

[Timer]
OnCalendar=Mon 08:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable with:
```bash
systemctl --user enable zeitgeist.timer
systemctl --user start zeitgeist.timer
```

### Output

Ideas are appended to `BACKLOG/ideas.yaml` with:
- Pillar assignment
- Status: seed
- Source: zeitgeist-YYYY-MM-DD
- Generated hook

A notification is sent via ntfy with a summary of new ideas.
