# Ideation Prompt

Instructions for generating content ideas for Grimshaw Studio.

---

## Step 1: Read BRAND Context

Before generating any ideas, **Read BRAND files** to internalize Mason's voice, audience, and content lanes:

1. `BRAND/voice.md` - Tone, signature moves, taboos
2. `BRAND/pillars.md` - The four content lanes and their audiences
3. `BRAND/voice-samples.md` - Real examples to calibrate against
4. `BRAND/do-dont.md` - Explicit guardrails
5. `BRAND/audience.md` - Who we're writing for

Also read the current backlog to avoid duplicates:

6. `BACKLOG/ideas.yaml` - Existing ideas and their statuses
7. `BACKLOG/parking-lot.md` - Overflow ideas not yet promoted

---

## Step 2: Source Raw Material

### Web Search (Preferred)

Use web search to scan for current AI zeitgeist across these categories:

- **Enterprise AI** - Production deployments, vendor announcements, analyst reports, CTO perspectives
- **Tribal / Indigenous AI** - Sovereignty initiatives, language preservation tech, tribal governance of data, Indigenous-led AI projects
- **Technical** - New architectures, papers, open-source releases, benchmark results
- **Culture & Fun** - Viral AI projects, creative experiments, unexpected applications, debates

Search queries to try:
- `AI enterprise production deployment this week`
- `Indigenous AI data sovereignty`
- `AI agent production failures lessons`
- `creative AI projects experiments`
- `AI news this week site:techcrunch.com OR site:theverge.com OR site:arstechnica.com`

Look for ideas that have a **contrarian angle** or **experience-grounded take** -- not just "X happened" but "X happened, and here's what everyone is missing."

### Fallback: When Web Search Is Unavailable

When web search is not available, generate ideas from these fallback sources:

1. **Personal experience** - Draw from consulting engagements, tribal community work, technical projects Mason has done
2. **Evergreen patterns** - Recurring problems in AI adoption that don't depend on news cycles (e.g., "the gap between demo and production")
3. **Existing backlog gaps** - Check which pillars are underrepresented in `ideas.yaml` and fill holes
4. **Technical fundamentals** - Deep dive topics that are always relevant (architecture patterns, data pipeline design, evaluation frameworks)
5. **Contrarian takes on conventional wisdom** - Challenge common AI narratives with grounded experience

The fallback approach should still produce high-quality ideas -- timeliness is a bonus, not a requirement.

---

## Step 3: Generate Ideas

For each idea, develop:

- **Title** - Specific, opinionated, not generic. "Agent Architectures That Ship" not "AI Agent Overview"
- **Pillar** - One of: `enterprise`, `tribal`, `deep-dive`, `experiments`
- **Hook** - One sentence that makes someone stop scrolling. Should contain a tension, surprise, or promise of insider knowledge
- **Notes** - Any supporting context, sources, connections to other ideas, or series potential

### Aim for Diversity

Each ideation session should produce ideas across multiple pillars. Don't cluster all ideas in one lane.

---

## Step 4: Score Each Idea

Rate every idea on four criteria (1-5 scale):

| Criterion | What It Measures | 5 = Best |
|-----------|-----------------|----------|
| **brand_fit** | Does this match Mason's voice, pillars, and audience? Would it feel natural on his site? | Perfect alignment with voice + pillar + audience |
| **novelty** | Is this a fresh angle, or has everyone already said this? | Genuinely new perspective or contrarian take |
| **artifact_potential** | Can this produce a compelling visual, interactive demo, simulation, or code artifact? | Rich artifact opportunity (visualization, interactive, live demo) |
| **effort** | How much work to produce? (Inverse: 5 = low effort, 1 = massive undertaking) | Quick to produce, high impact |

### Scoring Guidelines

- **brand_fit: 5** - Hits a pillar squarely, uses Mason's voice naturally, serves his target audience
- **brand_fit: 1** - Generic AI content anyone could write, no distinctive angle
- **novelty: 5** - Nobody else is saying this; contrarian or insider perspective
- **novelty: 1** - "AI is transforming business" level of obvious
- **artifact_potential: 5** - Natural fit for interactive visualization, simulation, or code demo
- **artifact_potential: 1** - Pure opinion piece, no visual or interactive element
- **effort: 5** - Can be written in one focused session (1-2 hours)
- **effort: 1** - Multi-week research project, original data collection required

Only promote ideas scoring **3+ on brand_fit** and **3+ on novelty** to the active backlog.

---

## Step 5: Add to ideas.yaml

Append qualifying ideas to `BACKLOG/ideas.yaml` using this exact YAML schema:

```yaml
- title: "The Title Goes Here"
  pillar: enterprise          # enterprise | tribal | deep-dive | experiments
  status: seed                # seed | researching | drafting | review | published | archived
  hook: "One compelling sentence that makes someone want to read this."
  notes: "Supporting context, sources, series potential, etc."
  added: 2026-01-15           # YYYY-MM-DD date added
```

### Field Requirements

- **title** (required): Specific and opinionated. Not "AI Trends" but "The Three AI Trends That Actually Matter for 2026"
- **pillar** (required): Must be one of the four defined pillars
- **status** (required): New ideas always start as `seed`
- **hook** (required): One sentence. Should contain tension, surprise, or promise. If you can't write a compelling hook, the idea isn't ready
- **notes** (optional): Context that will help when it's time to draft. Sources, data points, connections to other ideas
- **added** (required): Today's date in YYYY-MM-DD format

### Optional Fields

These fields may also appear on ideas (especially those generated by the zeitgeist scanner):

- **source**: Origin of the idea (e.g., `zeitgeist-2026-02-09`)

---

## Step 6: Manage Backlog Size

### Active Backlog: ideas.yaml

Keep **10-25 active ideas** in `BACKLOG/ideas.yaml` at any time. This is the sweet spot:

- **Fewer than 10**: Not enough options to choose from; feels constraining
- **More than 25**: Decision paralysis; ideas go stale before they're written

### Overflow: parking-lot.md

When the active backlog exceeds 25 ideas, move lower-scoring ideas to `BACKLOG/parking-lot.md`. The parking-lot is for:

- Ideas that scored well on one criterion but poorly on others
- "Someday/maybe" ideas that need more research or a news hook
- Ideas that are interesting but don't fit the current content cadence
- Series concepts that aren't ready to start yet

Format for parking-lot entries:

```markdown
## [Idea Title]
**Pillar:** enterprise | tribal | deep-dive | experiments
**Why parked:** [Brief reason - e.g., "needs a news hook", "too big for current cadence"]
**Notes:** [Any context worth preserving]
```

### Promoting from Parking Lot

During ideation sessions, scan the parking-lot for ideas whose time has come -- a news event that creates a hook, a completed project that provides source material, or a gap in the active backlog that the idea would fill.

---

## Summary Checklist

Before finishing an ideation session, verify:

- [ ] Read BRAND files first
- [ ] Sourced ideas from web search (or fallback methods)
- [ ] Generated ideas across multiple pillars
- [ ] Scored each idea on brand_fit, novelty, artifact_potential, and effort
- [ ] Added qualifying ideas to ideas.yaml with correct schema
- [ ] Active backlog is between 10-25 ideas
- [ ] Overflow moved to parking-lot.md if needed
- [ ] No duplicate ideas in the backlog
