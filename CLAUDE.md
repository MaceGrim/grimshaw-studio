# Grimshaw Studio

This is Mason Grimshaw's content studio - a system for generating thoughtful AI content with a distinctive voice.

## Content Generation

When drafting content (blog posts, articles, LinkedIn posts, talks, abstracts):

1. **Load brand context first** - Read these before drafting:
   - `BRAND/voice.md` - tone, signature moves, taboos
   - `BRAND/pillars.md` - which lane this fits
   - `BRAND/voice-samples.md` - real examples to match

2. **Infer the pillar** from the topic:
   - **Enterprise AI** → CTOs, production systems, "what actually works"
   - **Tribal AI** → Indigenous communities, sovereignty, capacity building
   - **Deep Dives** → Technical series, building from scratch
   - **Experiments** → Playful projects, visualizations, "let's find out"

3. **Match tone to pillar:**
   - Enterprise = serious, practical, grounded in real engagements
   - Tribal = accessible, honest, Indigenous-led framing (never savior)
   - Deep Dives = technical, thorough, assumes competence
   - Experiments = playful, curious, personality-forward

4. **Use voice samples as templates** - match the rhythm, framing, and honesty level

5. **Check taboos before finishing:**
   - No AI hype/breathlessness ("revolutionary", "game-changing")
   - No savior framing for tribal work
   - No generic advice ("leverage AI for competitive advantage")
   - No vendor pitches

## Backlog

Ideas live in `BACKLOG/ideas.yaml`.

- Add new ideas there when suggested or requested
- Each idea has: title, pillar, status, hook, notes, added date
- Status flow: `seed` → `researching` → `drafting` → `review` → `published`

## Project Structure

```
grimshaw-studio/
├── BRAND/
│   ├── voice.md           # Tone, signature moves, taboos
│   ├── voice-samples.md   # Real examples for reference
│   └── pillars.md         # Four content lanes
├── BACKLOG/
│   └── ideas.yaml         # Content pipeline
├── DRAFTS/                 # Work in progress
├── SITE/                   # Astro site (future)
└── TOOLS/                  # Scripts and automation
```

## Available Skills

- `/idea "topic"` - Quick-add idea to backlog
- `/backlog` - View and filter ideas
- `/draft "title"` - Load idea and start writing with voice context

## Automation: Zeitgeist Scanner

The `TOOLS/zeitgeist.py` script researches AI trends weekly across four categories:
- **Social** - Viral discussions, debates, cultural moments
- **Tribal** - Indigenous AI, sovereignty, tribal tech
- **Enterprise** - Production deployments, case studies
- **Fun** - Creative projects, experiments, inspiration

### Running the Scanner

```bash
cd TOOLS

# Dry run (preview without saving)
python zeitgeist.py --dry-run

# Full scan - saves to BACKLOG/ideas.yaml
python zeitgeist.py

# Also create Todoist tasks for the week
python zeitgeist.py --create-tasks

# Single category only
python zeitgeist.py --category tribal
```

### Todoist Integration

The `--create-tasks` flag creates weekly content tasks directly via the Todoist API (more reliable than the MCP server which can timeout).

**Setup:**
1. Get API token: https://todoist.com/app/settings/integrations/developer
2. Set environment variable: `export TODOIST_API_TOKEN=your-token`
3. (Optional) Create a "Content Studio" project in Todoist

**Tasks created each Monday:**
- Review zeitgeist ideas (Monday)
- LinkedIn post #1 (Tuesday 9am)
- LinkedIn post #2 (Thursday 9am)
- Draft flagship blog post (Friday 2pm)

### Weekly Cron Setup

Add to crontab to run every Monday at 8 AM:
```bash
0 8 * * 1 cd /path/to/grimshaw-studio/TOOLS && python3 zeitgeist.py --create-tasks >> /tmp/zeitgeist.log 2>&1
```

## Content Cadence

| Tier | Format | Frequency | Purpose |
|------|--------|-----------|---------|
| **Flagship** | Blog post (1500+ words) | 2x/month | Depth, SEO, speaking credibility |
| **Signal** | LinkedIn (200-400 words) | 2-3x/week | Visibility, network building |
| **Spark** | Quick takes, shares | As needed | Stay in the feed |

**What goes where:**
- Flagship: Enterprise frameworks, Tribal perspective pieces, Deep dives
- Signal: Zeitgeist reactions, consulting lessons, tribal news
- Spark: Fun experiments, reshares with commentary
