# Grimshaw Studio - Content Production System

## Project Overview

A lightweight, GitHub-Pages-based content studio that enables Mason Grimshaw to consistently produce thoughtful AI content and beautiful technical artifacts with high leverage from Claude Code. The system encodes brand voice, generates and manages ideas, scaffolds drafts with artifacts, supports review, and publishes to a static site.

**Core Principle:** Claude Code is the primary operator. The system must be readable, writable, and navigable by an AI assistant working in short sessions.

---

## Brand Identity

### Positioning
Mason Grimshaw: Enterprise AI partner with a distinctive tribal lens. A systems thinker who builds beautiful, complex things and cuts through hype with grounded skepticism.

**Single unified brand** - tribal AI perspectives are a differentiation pillar, not a separate identity. The Lakota background, MIT data science training, and environmental/consulting experience form a unique combination that commands premium positioning.

### Target Audience
- Enterprise AI decision-makers (CTO, VP Engineering, AI leads)
- Speaking event organizers ($10k+ engagements)
- Technical practitioners who appreciate depth and craft
- (Secondary) Tribal communities interested in AI sovereignty

### Signature Moves
1. **Systems thinking lens** - See interconnections others miss, make complex understandable
2. **Visual/artifact-first** - Show don't tell; lead with the simulation, the chart, the interactive thing
3. **Grounded skepticism** - Cut through hype with "here's what actually works"
4. **Storytelling from experience** - Real examples from consulting work, tribal community, daily life

### Taboos (Nuanced)
- **AI hype/breathlessness** - No "AGI is coming" or "AI will change everything." Grounded takes only.
- **Savior framing** - Never position as "bringing AI to help the natives." Dignity always.
- **Performative futurism** - No "imagine a world where..." speculation without substance.
- **Generic AI advice** - No "5 ways to use ChatGPT" listicles. Only what's distinctly Mason's.

**Nuance:** Topics aren't off-limits, it's about *how* they're approached:
- Indigenous AI futures are fine if framed around sovereignty and self-determination
- Novel Claude Code/ChatGPT uses are fine if genuinely novel
- Difficult tribal topics can be explored with care and dignity

---

## Content Strategy

### Cadence
**Thoughtful content every other week** - All content counts toward this cadence, including "fun" projects.

### Content Lanes
| Lane | Description | Audience |
|------|-------------|----------|
| Enterprise AI/Agents | Production AI systems, architecture, practical implementation | Decision-makers, practitioners |
| Tribal AI | Sovereignty, stewardship, capacity-building through technology | Tribal leaders, allies, tech folks |
| Technical Deep Dives | Multi-part series on hard problems (transformers from scratch, etc.) | Practitioners, peers |
| Experiments/Fun | RimWorld agents, sports analytics, playful technical projects | Everyone, demonstrates range |

### Content Modes
**Curiosity Posts (Small/Medium)**
- Quick ideas, observations, single-visualization pieces
- Can complete in 2-3 short sessions
- Hook → Insight → Artifact → Takeaway structure

**Deep Pieces (Large)**
- Multi-part series, 3-5 posts each
- Substantial technical depth
- **Must finish what you start** - commitment to audience
- Each post should be valuable standalone even if series doesn't complete

### Series Approach
- Scope series to 3-5 posts before starting
- Define north star, post arc, consistent terminology upfront
- System tracks series metadata for continuity
- If blocked on a series, pause is acceptable but abandonment is not

---

## Ideation System

### Dual-Mode Ideation
1. **Claude proposes** - Generates ideas based on web search (zeitgeist, trending AI topics), brand guidelines, and pattern matching
2. **Mason adds** - Captures ideas from anywhere (conversations, papers, observations) into the backlog

### Idea Sources
- Current AI news and discourse (Claude searches)
- Technical papers and tools encountered at work
- Personal observations from consulting and community
- Interesting phenomena in the world worth visualizing

### Backlog Management
- **10-25 active ideas** in the main backlog
- Parking lot for overflow/someday-maybe
- Status tracking: `proposed` → `selected` → `in-progress` → `published`
- Each idea scores for: brand fit, novelty, artifact potential, effort level

### Idea Schema
```yaml
id: unique-slug
title: "Human-readable title"
lane: enterprise-ai | tribal-ai | deep-dive | experiments
effort: small | medium | large
hook: "Why should anyone care? One sentence."
audience: "Who is this for?"
artifacts: ["list", "of", "required", "artifacts"]
series: optional-series-id
status: proposed | selected | in-progress | published
created: 2024-01-15
notes: "Any additional context"
```

---

## Workflow

### High-Level Flow
```
Brand Reference → Ideation → Selection → Draft + Artifacts → Review → Repurpose → Publish
```

**Flexible within structure:** Stages exist and should be followed, but Mason can move around when inspiration strikes. System supports jumping to any stage.

### Typical Session (15-30 minutes)
Sessions make incremental progress on one piece:
- Review and approve Claude's prep work
- Move a post from outline to partial draft
- Edit voice in a generated draft
- Complete a small piece end-to-end (rare for larger pieces)

### Stage Details

**1. Brand Reference (Always First)**
Claude reads BRAND folder before any generation. Non-negotiable.

**2. Ideation**
- Claude generates ideas (web search enabled)
- Scores for brand fit, novelty, artifact potential
- Updates ideas.yaml with new entries

**3. Selection**
Mason manually chooses which idea to work on. System creates project folder.

**4. Draft + Artifact Creation**
Claude scaffolds:
- `brief.md` - Scope, audience, key points
- `outline.md` - Structure and flow
- `draft.md` - Full written draft (canonical source of truth)
- `artifacts/` - Visualizations, simulations, charts

**5. Review**
Review is tests, not vibes. Checklist includes:
- [ ] Voice consistency - sounds like Mason
- [ ] Technical accuracy - claims correct, code runs
- [ ] Artifact quality - visualizations work and look good
- [ ] Has a hook - why should anyone read this?
- [ ] Hits brand pillars appropriately

Claude suggests edits without overwriting. Mason approves all changes.

**6. Repurpose**
Generate platform variants:
- LinkedIn post (professional, slightly longer)
- (Future) Twitter thread
- (Future) Newsletter section

**7. Publish**
- Move final content to SITE folder
- Deploy via GitHub Pages
- Prepare posting checklist for manual distribution

### Canonical Content Rule
- `draft.md` = single source of truth
- Platform variants are derived outputs
- Mason edits canonical draft only

---

## Technical Architecture

### Stack
- **Site:** Astro + MDX on GitHub Pages
- **Styling:** Tailwind CSS (small design system)
- **Visualizations:** p5.js, D3.js, Canvas (Claude does heavy lifting)
- **Data:** DuckDB / static CSVs for analysis artifacts
- **Future:** Remotion for video exports (not required initially)

### Constraints
- Static only - no backend, no databases, no serverless functions
- Plain text files - deterministic folder structure Claude can navigate
- Git history sufficient for versioning
- Some live API data okay in visualizations (public APIs only)

### Artifact Requirements
- **Must work before publishing** - no broken visualizations go live
- Graceful degradation encouraged (static fallback images)
- Style guidance per piece: templates + examples + mood words

### Visual Style System
**Templates** (3-4 modes to choose from):
- Playful/animated - movement, color, delightful interactions
- Technical/dense - Tufte-inspired, information-rich
- Minimal/stark - whitespace, subtle animations
- (Additional templates added as needed)

**Per-piece guidance:**
- Example images/links Claude should match
- Mood words ("serious," "whimsical," "stark")
- Specific constraints ("must work on mobile")

---

## Repository Structure

```
grimshaw-studio/
├── BRAND/
│   ├── voice.md              # Tone, signature moves, taboos
│   ├── pillars.md            # Content pillars and positioning
│   ├── style.md              # Writing style guidelines
│   ├── do-dont.md            # Quick reference guardrails
│   ├── audience.md           # Target audience profiles
│   ├── examples/             # Example posts, good and bad
│   └── visuals/
│       ├── palette.md        # Colors and usage
│       ├── typography.md     # Fonts and hierarchy
│       └── components/       # Reusable visual components
├── BACKLOG/
│   ├── ideas.yaml            # Active idea backlog (10-25 items)
│   ├── series.yaml           # Multi-part series metadata
│   └── parking-lot.md        # Overflow/someday-maybe ideas
├── PROJECTS/
│   └── <slug>/
│       ├── brief.md          # Scope and requirements
│       ├── outline.md        # Structure and flow
│       ├── draft.md          # Canonical written content
│       ├── artifacts/        # Visualizations, data, code
│       ├── platforms/        # LinkedIn, Twitter variants
│       └── review/
│           ├── checklist.md  # Quality checks
│           ├── edits.md      # Suggested changes
│           └── notes.md      # Review feedback
├── SITE/
│   └── src/                  # Astro site source
├── PROMPTS/
│   ├── 00-system.md          # Core operating rules for Claude
│   ├── 10-ideate.md          # Idea generation instructions
│   ├── 30-draft.md           # Drafting instructions
│   ├── 40-artifacts.md       # Visualization creation
│   ├── 50-review.md          # Review checklist runner
│   ├── 60-repurpose.md       # Platform variant generation
│   └── 70-publish.md         # Publishing workflow
├── scripts/                   # Utility scripts
├── Makefile                   # Common commands
└── README.md                  # Project overview
```

---

## Publishing & Platforms

### Primary Platforms
1. **Personal site** (grimshaw-studio deployed to GitHub Pages)
2. **LinkedIn** (professional audience, speaking opportunities)

### Future Platforms (not in MVP)
- Twitter/X
- Newsletter (email capture)
- YouTube (video essays from Remotion)

### Domain & Migration
**Existing site:** `macegrim.github.io` - Jekyll-based portfolio (academicpages theme) with:
- `_talks/` - Speaking history (TedX, NeurIPS, etc.)
- `_portfolio/` - Project showcases
- `_publications/` - Academic publications
- `_posts/` - Blog (placeholder content)
- `_teaching/` - Teaching materials
- D3 visualizations in assets

**Local path:** `/mnt/o/Mason/Github/macegrim.github.io`

**Strategy:** Migrate existing site to Astro, adding content studio workflow. Single unified system at the same URL.

**Repo Strategy:** `grimshaw-studio` is the working repo. Deploys to `macegrim.github.io` via GitHub Actions.

**Migration scope:**
- Port existing collections (_talks, _portfolio, _publications) to Astro content collections in grimshaw-studio
- Preserve existing D3 visualizations
- Add BRAND/, BACKLOG/, PROJECTS/ structure
- Blog section becomes the content studio output
- GitHub Action pushes built site to macegrim.github.io repo
- Old Jekyll repo preserved as archive/backup

---

## Success Criteria

### The system is working when:
1. Mason says "Generate ideas" → gets usable, on-brand backlog entries
2. Selecting an idea → produces structured project folder with scaffolded content
3. Artifacts and writing feel on-brand without heavy rewriting
4. Voice misses are fixable with editing, not restarts
5. Publishing is boring (just moving files and clicking post)

### Quality bar:
- Every published piece demonstrates at least one signature move
- Visualizations work on desktop and mobile
- No broken links, no 404s, no console errors
- Content would impress a CTO enough to consider a speaking engagement

---

## Scope Boundaries

### In Scope (MVP)
- Full folder structure with all BRAND files
- Working ideation with web search
- Draft + artifact generation
- Review checklist system
- **Migrate existing macegrim.github.io to Astro**
- Preserve portfolio and speaking sections
- LinkedIn repurposing
- One complete end-to-end example post published to migrated site

### Out of Scope (Future)
- Email newsletter integration
- Custom domain
- Twitter/X automation
- Video generation (Remotion)
- Analytics dashboard
- Collaboration features (editors, guest posts)
- Mobile app

---

## Open Questions

1. **Visual examples:** Need to collect 10-20 screenshots of visualizations Mason loves to train Claude's aesthetic sense
2. **LinkedIn posting:** Manual for now, but could explore scheduling tools later
3. **Backlog seeding:** Initial 5-10 ideas to populate the system
4. **Artifact testing:** Need a reliable way to verify p5.js/D3 visualizations work before publishing

---

## Assumptions

1. Mason has Node.js and npm available for Astro development
2. GitHub account exists and can host Pages
3. 15-30 minute sessions 2-4 times per week is realistic
4. Claude Code can reliably execute web searches for ideation
5. p5.js/D3/Canvas skills will develop over time with Claude's help

---

## Tooling Architecture

The system requires different types of tooling for different purposes:

### Claude Code Skills (User Commands)

Skills are invoked with `/skill-name` and run interactively. These are for **workflow stages** that benefit from conversation:

| Skill | Purpose | Invocation |
|-------|---------|------------|
| `/studio-ideate` | Generate new ideas, score for brand fit, update backlog | When you want fresh ideas |
| `/studio-draft` | Create project folder, scaffold brief/outline/draft | After selecting an idea |
| `/studio-artifact` | Generate visualization code with testing | When draft needs interactive elements |
| `/studio-review` | Run checklist, suggest edits | Before publishing |
| `/studio-repurpose` | Generate LinkedIn variant | After review passes |
| `/studio-publish` | Move to SITE, prepare posting checklist | Final step |

**Why skills:** These are conversational, may need clarification, benefit from incremental progress in 15-30 minute sessions.

### Claude Code Hooks (Automatic Guardrails)

Hooks run automatically before/after tool calls. Use for **enforcement** that should never be skipped:

| Hook | Trigger | Purpose |
|------|---------|---------|
| `pre-write-brand-check` | Before any Write to PROJECTS/ | Verify BRAND folder was read this session |
| `post-artifact-test` | After Write to artifacts/ | Run artifact to verify it executes without error |
| `pre-publish-checklist` | Before moving to SITE/ | Ensure review checklist passed |

**Why hooks:** These enforce rules automatically. Can't forget to read brand guidelines, can't publish broken visualizations.

### Scripts (Reusable Utilities)

Scripts are standalone tools for **non-conversational tasks**:

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/test-artifact.sh` | Run a p5.js/D3 visualization headlessly, check for errors | Called by hooks or manually |
| `scripts/validate-yaml.sh` | Ensure ideas.yaml and series.yaml are valid | Pre-commit hook |
| `scripts/build-site.sh` | Build Astro site, run local preview | Development |
| `scripts/deploy.sh` | Deploy to GitHub Pages | After publish |
| `scripts/lint-brand.sh` | Check draft against brand voice patterns | Optional review step |

**Why scripts:** Deterministic, testable, can run outside Claude Code sessions.

### Makefile (Convenience)

Common command patterns:

```makefile
ideate:       # Run ideation skill
draft ID:     # Start drafting idea by ID
review SLUG:  # Review a project
publish SLUG: # Publish a project
preview:      # Local site preview
deploy:       # Deploy to GitHub Pages
test:         # Run all artifact tests
lint:         # Validate YAML, check brand compliance
```

**Why Makefile:** Standardizes commands, discoverable, works across sessions.

### PROMPTS/ Folder (Claude Context Loaders)

Not executable, but critical for Claude Code operation. These are **context documents** that skills read before operating:

```
PROMPTS/
├── 00-system.md     # Core rules: read BRAND first, never overwrite, etc.
├── 10-ideate.md     # How to generate ideas, scoring criteria
├── 30-draft.md      # Drafting approach, structure templates
├── 40-artifacts.md  # Visualization patterns, testing requirements
├── 50-review.md     # Checklist items, how to suggest edits
├── 60-repurpose.md  # Platform constraints (LinkedIn character limits, etc.)
└── 70-publish.md    # Publishing steps, deployment process
```

**Why separate files:** Skills read the relevant prompt before operating. Keeps context modular and editable.

### Tool Integration Summary

```
User invokes:     /studio-draft some-idea
                        │
Skill reads:      PROMPTS/00-system.md + PROMPTS/30-draft.md + BRAND/*
                        │
Hook fires:       pre-write-brand-check (verifies BRAND was read)
                        │
Claude writes:    PROJECTS/some-idea/brief.md, outline.md, draft.md
                        │
If artifacts:     Claude writes to artifacts/
                        │
Hook fires:       post-artifact-test → scripts/test-artifact.sh
                        │
If error:         Claude sees output, fixes, tries again
                        │
Session ends:     Progress saved, resume later with /studio-draft continue
```

---

## Implementation Notes

This system is designed for Claude Code to operate. Key principles:

1. **Read BRAND first** - Every generation session starts with brand context
2. **Never overwrite Mason's edits** - Suggestions go in review/ files
3. **Prefer options over questions** - Present choices, don't ask open-ended
4. **Test artifacts** - Verify visualizations run before proposing
5. **Incremental progress** - Sessions are short, design for interruptibility
