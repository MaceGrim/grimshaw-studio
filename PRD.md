# Grimshaw Studio - Product Requirements Document

## Executive Summary

Grimshaw Studio is a Claude Code-operated content production system that enables Mason Grimshaw to consistently publish thoughtful AI content and beautiful interactive artifacts. The system migrates his existing Jekyll-based portfolio site to Astro, adding structured ideation, drafting, review, and publishing workflows. Claude Code is the primary operator, working within a deterministic folder structure with brand guidelines as the source of truth.

The goal is bi-weekly thoughtful content that builds Mason's reputation as an enterprise AI partner with a distinctive tribal lens, commanding $10k+ speaking engagements.

## Problem Statement

Mason has the expertise and positioning to be a thought leader in enterprise AI (MIT data science background, tribal AI perspective, consulting experience), but lacks a consistent system for producing content. The current Jekyll portfolio site has placeholder blog content and no workflow for ideation-to-publication. Content creation is ad-hoc, making it hard to maintain the every-other-week cadence needed to build speaking reputation.

**Pain points:**
- No structured ideation system to capture and develop ideas
- No brand guidelines encoded anywhere (voice, taboos, signature moves)
- Manual, inconsistent process from idea to published piece
- Visualization creation is time-consuming without templates or scaffolding
- No review process to ensure quality and brand consistency

## Target Users

### Primary: Mason Grimshaw (Content Creator)
- **Goal:** Publish thoughtful content bi-weekly that builds enterprise AI speaking reputation
- **Context:** 15-30 minute work sessions, uses Claude Code as primary operator
- **Pain:** Ad-hoc content creation, no consistency, visualization creation is slow

### Secondary: Claude Code (Operator)
- **Goal:** Execute content workflows reliably with minimal human intervention
- **Context:** Reads brand guidelines, navigates folder structure, generates content
- **Pain:** Needs deterministic structure, clear prompts, testable artifacts

### Tertiary: Enterprise AI Decision-Makers (Audience)
- **Goal:** Find thought leaders worth booking for speaking engagements
- **Context:** Browse LinkedIn, personal sites looking for depth and craft
- **Pain:** Most AI content is generic hype; seeking grounded, substantive perspectives

---

## User Stories

### Epic 1: Repository & Migration Setup

#### US-001: Initialize Repository Structure
**As a** content creator **I want to** have a complete folder structure with all required directories and placeholder files **so that** Claude Code can immediately navigate and operate within the system.

**Acceptance Criteria:**
- [ ] BRAND/ directory exists with voice.md, pillars.md, style.md, do-dont.md, audience.md
- [ ] BRAND/visuals/ directory exists with palette.md, typography.md
- [ ] BRAND/visuals/components/ directory exists
- [ ] BRAND/examples/ directory exists
- [ ] BACKLOG/ directory exists with ideas.yaml, series.yaml, parking-lot.md
- [ ] PROJECTS/ directory exists
- [ ] PROMPTS/ directory exists with 00-system.md, 10-ideate.md, 30-draft.md, 40-artifacts.md, 50-review.md, 60-repurpose.md, 70-publish.md
- [ ] PROMPTS/skills/ directory exists
- [ ] scripts/ directory exists
- [ ] scripts/fixtures/ directory exists
- [ ] Makefile exists
- [ ] README.md exists
- [ ] .github/workflows/ directory exists

**Verification:**
```bash
test -d BRAND && \
test -f BRAND/voice.md && \
test -f BRAND/pillars.md && \
test -f BRAND/style.md && \
test -f BRAND/do-dont.md && \
test -f BRAND/audience.md && \
test -d BRAND/visuals && \
test -f BRAND/visuals/palette.md && \
test -f BRAND/visuals/typography.md && \
test -d BRAND/visuals/components && \
test -d BRAND/examples && \
test -d BACKLOG && \
test -f BACKLOG/ideas.yaml && \
test -f BACKLOG/series.yaml && \
test -f BACKLOG/parking-lot.md && \
test -d PROJECTS && \
test -d PROMPTS && \
test -f PROMPTS/00-system.md && \
test -f PROMPTS/10-ideate.md && \
test -f PROMPTS/30-draft.md && \
test -f PROMPTS/40-artifacts.md && \
test -f PROMPTS/50-review.md && \
test -f PROMPTS/60-repurpose.md && \
test -f PROMPTS/70-publish.md && \
test -d PROMPTS/skills && \
test -d scripts && \
test -d scripts/fixtures && \
test -f Makefile && \
test -f README.md && \
test -d .github/workflows && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-002: Initialize Astro Site
**As a** content creator **I want to** have a working Astro site in SITE/ **so that** content can be built and previewed locally.

**Acceptance Criteria:**
- [ ] SITE/package.json exists and contains "astro" in dependencies
- [ ] SITE/package.json contains "tailwindcss" in dependencies
- [ ] SITE/tailwind.config.mjs (or .js/.cjs) exists
- [ ] `npm install` in SITE/ completes with exit code 0
- [ ] `npm run build` in SITE/ completes with exit code 0
- [ ] SITE/dist/ directory is created after build

**Verification:**
```bash
cd SITE && \
grep -q '"astro"' package.json && \
grep -q 'tailwindcss' package.json && \
(test -f tailwind.config.mjs || test -f tailwind.config.js || test -f tailwind.config.cjs) && \
npm install && \
npm run build && \
test -d dist && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-003: Migrate Existing Content Collections
**As a** content creator **I want to** have my existing talks, portfolio, and publications migrated to Astro content collections **so that** my existing content is preserved and accessible.

**Acceptance Criteria:**
- [ ] SITE/src/content/talks/ directory exists with .md files
- [ ] Number of files in SITE/src/content/talks/ >= number of files in source _talks/
- [ ] SITE/src/content/portfolio/ directory exists with .md files
- [ ] Number of files in SITE/src/content/portfolio/ >= number of files in source _portfolio/
- [ ] SITE/src/content/publications/ directory exists with .md files
- [ ] SITE/src/content/config.ts defines schemas for talks, portfolio, publications, blog
- [ ] SITE/public/artifacts/legacy/ directory exists (D3 visualizations copied if present in source)
- [ ] Site builds without errors and generates HTML for each collection

**Verification:**
```bash
cd SITE && \
test -d src/content/talks && \
test -d src/content/portfolio && \
test -d src/content/publications && \
test -f src/content/config.ts && \
grep -q "talks" src/content/config.ts && \
grep -q "portfolio" src/content/config.ts && \
grep -q "blog" src/content/config.ts && \
test -d public/artifacts/legacy && \
npm run build && \
test -f dist/index.html && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-004: Configure GitHub Actions Deployment
**As a** content creator **I want to** have automated deployment to macegrim.github.io **so that** publishing is a single command.

**Acceptance Criteria:**
- [ ] .github/workflows/deploy.yml exists
- [ ] Workflow triggers on push to main branch
- [ ] Workflow uses actions/checkout and withastro/action
- [ ] Workflow pushes to external repository macegrim/macegrim.github.io
- [ ] Workflow uses DEPLOY_TOKEN secret (not hardcoded)
- [ ] README.md documents: (1) create a PAT with repo scope, (2) add as DEPLOY_TOKEN secret

**Verification:**
```bash
test -f .github/workflows/deploy.yml && \
grep -q 'push:' .github/workflows/deploy.yml && \
grep -q 'main' .github/workflows/deploy.yml && \
grep -q 'astro' .github/workflows/deploy.yml && \
grep -q 'DEPLOY_TOKEN' .github/workflows/deploy.yml && \
grep -q 'DEPLOY_TOKEN' README.md && \
! grep -qE 'ghp_[a-zA-Z0-9]+' .github/workflows/deploy.yml && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

### Epic 2: Brand System

#### US-005: Create Voice Guidelines
**As** Claude Code **I want to** read comprehensive voice guidelines from BRAND/voice.md **so that** all generated content matches Mason's distinctive voice.

**Acceptance Criteria:**
- [ ] voice.md contains "Tone:" section with slider settings
- [ ] voice.md contains "Systems thinking" as signature move with example
- [ ] voice.md contains "Visual/artifact-first" as signature move with example
- [ ] voice.md contains "Grounded skepticism" as signature move with example
- [ ] voice.md contains "Storytelling" as signature move with example
- [ ] voice.md contains "Taboos:" section listing AI hype, savior framing, performative futurism
- [ ] voice.md contains "Nuance:" section explaining when taboo topics ARE okay
- [ ] voice.md contains at least 3 example sentences demonstrating voice

**Verification:**
```bash
grep -q "Tone:" BRAND/voice.md && \
grep -q "Systems thinking" BRAND/voice.md && \
grep -q "Visual" BRAND/voice.md && \
grep -q "Grounded skepticism" BRAND/voice.md && \
grep -q "Storytelling" BRAND/voice.md && \
grep -q "Taboos:" BRAND/voice.md && \
grep -q "hype" BRAND/voice.md && \
grep -q "savior" BRAND/voice.md && \
grep -q "Nuance:" BRAND/voice.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-006: Create Content Pillars Document
**As** Claude Code **I want to** read content pillars from BRAND/pillars.md **so that** generated ideas align with strategic positioning.

**Acceptance Criteria:**
- [ ] pillars.md contains "Enterprise AI" lane with "Audience:" field
- [ ] pillars.md contains "Tribal AI" lane with "Audience:" field
- [ ] pillars.md contains "Deep Dives" lane with "Audience:" field
- [ ] pillars.md contains "Experiments" lane with "Audience:" field
- [ ] Each lane has at least 2 example topics listed
- [ ] pillars.md contains section on how content supports speaking positioning

**Verification:**
```bash
grep -q "Enterprise AI" BRAND/pillars.md && \
grep -q "Tribal AI" BRAND/pillars.md && \
grep -q "Deep Dives" BRAND/pillars.md && \
grep -q "Experiments" BRAND/pillars.md && \
grep -c "Audience:" BRAND/pillars.md | grep -q "4" && \
grep -q "speaking" BRAND/pillars.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-007: Create Audience Profiles
**As** Claude Code **I want to** read audience profiles from BRAND/audience.md **so that** content targets the right readers.

**Acceptance Criteria:**
- [ ] audience.md defines primary audience with "Goals:", "Pain points:", "Looking for:" sections
- [ ] audience.md mentions CTO, VP Engineering, or AI leads
- [ ] audience.md defines secondary audience (practitioners)
- [ ] audience.md defines tertiary audience (tribal communities)
- [ ] audience.md includes "What impresses them:" section

**Verification:**
```bash
grep -q "Goals:" BRAND/audience.md && \
grep -q "Pain points:" BRAND/audience.md && \
grep -qE "(CTO|VP|decision-maker)" BRAND/audience.md && \
grep -q "practitioner" BRAND/audience.md && \
grep -q "tribal" BRAND/audience.md && \
grep -q "impress" BRAND/audience.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

#### US-008: Create Visual Style Guide
**As** Claude Code **I want to** read visual guidelines from BRAND/visuals/ **so that** generated artifacts match Mason's aesthetic.

**Acceptance Criteria:**
- [ ] palette.md defines at least 3 colors with hex codes (format: #XXXXXX)
- [ ] palette.md explains usage for each color
- [ ] typography.md specifies heading font family
- [ ] typography.md specifies body font family
- [ ] typography.md defines size hierarchy (h1, h2, h3, body)
- [ ] Either palette.md or typography.md defines three visual modes: playful, technical, minimal

**Verification:**
```bash
test $(grep -cE '#[0-9A-Fa-f]{6}' BRAND/visuals/palette.md) -ge 3 && \
grep -q "heading" BRAND/visuals/typography.md && \
grep -q "body" BRAND/visuals/typography.md && \
(grep -q "playful" BRAND/visuals/palette.md || grep -q "playful" BRAND/visuals/typography.md) && \
(grep -q "technical" BRAND/visuals/palette.md || grep -q "technical" BRAND/visuals/typography.md) && \
(grep -q "minimal" BRAND/visuals/palette.md || grep -q "minimal" BRAND/visuals/typography.md) && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

### Epic 3: Ideation System

#### US-009: Create Ideation Prompt
**As** Claude Code **I want to** have clear instructions in PROMPTS/10-ideate.md **so that** I can generate on-brand ideas.

**Acceptance Criteria:**
- [ ] 10-ideate.md begins with instruction to read BRAND/* files
- [ ] 10-ideate.md explains web search can be used for zeitgeist topics
- [ ] 10-ideate.md defines fallback when web search unavailable (use recent tech news, personal observations)
- [ ] 10-ideate.md defines scoring criteria: brand_fit, novelty, artifact_potential, effort
- [ ] 10-ideate.md shows exact YAML format for ideas.yaml entries with all fields
- [ ] 10-ideate.md explains difference between ideas.yaml (10-25 active) and parking-lot.md (overflow)

**Verification:**
```bash
grep -q "Read BRAND" PROMPTS/10-ideate.md && \
grep -q "web search" PROMPTS/10-ideate.md && \
grep -q "fallback" PROMPTS/10-ideate.md && \
grep -q "brand_fit" PROMPTS/10-ideate.md && \
grep -q "novelty" PROMPTS/10-ideate.md && \
grep -q "ideas.yaml" PROMPTS/10-ideate.md && \
grep -q "parking-lot" PROMPTS/10-ideate.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-010: Seed Initial Ideas Backlog
**As a** content creator **I want to** have 5-10 starter ideas in ideas.yaml **so that** I can immediately select one to work on.

**Acceptance Criteria:**
- [ ] ideas.yaml is valid YAML (parseable)
- [ ] ideas.yaml contains at least 5 idea entries
- [ ] Each entry has required fields: id, title, lane, effort, hook, audience, artifacts, status, created
- [ ] Ideas span at least 2 different content lanes
- [ ] At least 1 idea has effort: small
- [ ] At least 1 idea has effort: medium
- [ ] At least 1 idea has effort: large
- [ ] All status values are one of: proposed, selected, in-progress, published

**Verification:**
```bash
python3 << 'EOF'
import yaml
import sys

try:
    with open('BACKLOG/ideas.yaml') as f:
        data = yaml.safe_load(f)

    if not isinstance(data, list) or len(data) < 5:
        print("FAIL: need at least 5 ideas")
        sys.exit(1)

    required = {'id', 'title', 'lane', 'effort', 'hook', 'audience', 'artifacts', 'status', 'created'}
    valid_status = {'proposed', 'selected', 'in-progress', 'published'}
    valid_effort = {'small', 'medium', 'large'}

    lanes = set()
    efforts = set()

    for i, idea in enumerate(data):
        missing = required - set(idea.keys())
        if missing:
            print(f"FAIL: idea {i} missing fields: {missing}")
            sys.exit(1)
        if idea['status'] not in valid_status:
            print(f"FAIL: idea {i} invalid status: {idea['status']}")
            sys.exit(1)
        if idea['effort'] not in valid_effort:
            print(f"FAIL: idea {i} invalid effort: {idea['effort']}")
            sys.exit(1)
        lanes.add(idea['lane'])
        efforts.add(idea['effort'])

    if len(lanes) < 2:
        print(f"FAIL: need at least 2 lanes, got {lanes}")
        sys.exit(1)

    if efforts != valid_effort:
        print(f"FAIL: need small, medium, and large efforts, got {efforts}")
        sys.exit(1)

    print("PASS")
except Exception as e:
    print(f"FAIL: {e}")
    sys.exit(1)
EOF
```

**Priority:** P1

---

#### US-011: Create Studio-Ideate Skill
**As a** content creator **I want to** run `/studio-ideate` to generate new ideas **so that** my backlog stays fresh.

**Note on Skills:** Claude Code skills are markdown prompt files that are invoked via `/skill-name`. They are NOT executable scripts. When a user types `/studio-ideate`, Claude Code reads the corresponding .md file and follows its instructions. The setup script creates symlinks so Claude Code can discover these skills.

**Acceptance Criteria:**
- [ ] Skill definition exists in PROMPTS/skills/studio-ideate.md (repo-local)
- [ ] Setup script scripts/setup-skills.sh exists and creates symlink to ~/.claude/commands/
- [ ] Skill content references reading BRAND/* files first
- [ ] Skill content references web search for trending topics
- [ ] Skill content references updating ideas.yaml
- [ ] Skill content references displaying generated ideas

**Verification:**
```bash
test -f PROMPTS/skills/studio-ideate.md && \
test -f scripts/setup-skills.sh && \
grep -q "BRAND" PROMPTS/skills/studio-ideate.md && \
grep -q "search" PROMPTS/skills/studio-ideate.md && \
grep -q "ideas.yaml" PROMPTS/skills/studio-ideate.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

### Epic 4: Drafting System

#### US-012: Create Drafting Prompt
**As** Claude Code **I want to** have clear instructions in PROMPTS/30-draft.md **so that** I can scaffold complete project folders.

**Acceptance Criteria:**
- [ ] 30-draft.md explains project folder structure: brief.md, outline.md, draft.md, artifacts/, platforms/, review/
- [ ] 30-draft.md defines brief.md format with sections: Scope, Audience, Key Points, Artifacts Needed
- [ ] 30-draft.md defines outline.md format with sections: Hook, Main Sections, Takeaway
- [ ] 30-draft.md defines "curiosity" mode: shorter (500-1000 words), single artifact, 2-3 sessions
- [ ] 30-draft.md defines "deep" mode: longer (2000+ words), multiple artifacts, part of series
- [ ] 30-draft.md references BRAND/voice.md for tone guidance
- [ ] 30-draft.md explains how to update idea status to "in-progress"

**Verification:**
```bash
grep -q "brief.md" PROMPTS/30-draft.md && \
grep -q "outline.md" PROMPTS/30-draft.md && \
grep -q "draft.md" PROMPTS/30-draft.md && \
grep -q "artifacts/" PROMPTS/30-draft.md && \
grep -q "review/" PROMPTS/30-draft.md && \
grep -q "Scope" PROMPTS/30-draft.md && \
grep -q "curiosity" PROMPTS/30-draft.md && \
grep -q "deep" PROMPTS/30-draft.md && \
grep -q "voice.md" PROMPTS/30-draft.md && \
grep -q "in-progress" PROMPTS/30-draft.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-013: Create Studio-Draft Skill
**As a** content creator **I want to** run `/studio-draft <idea-id>` to scaffold a project **so that** I can start writing immediately.

**Acceptance Criteria:**
- [ ] Skill definition exists in PROMPTS/skills/studio-draft.md
- [ ] Skill references creating PROJECTS/<slug>/ directory
- [ ] Skill references creating brief.md, outline.md, draft.md
- [ ] Skill references creating artifacts/ and review/ subdirectories
- [ ] Skill references updating idea status in ideas.yaml

**Verification:**
```bash
test -f PROMPTS/skills/studio-draft.md && \
grep -q "PROJECTS" PROMPTS/skills/studio-draft.md && \
grep -q "brief.md" PROMPTS/skills/studio-draft.md && \
grep -q "outline.md" PROMPTS/skills/studio-draft.md && \
grep -q "draft.md" PROMPTS/skills/studio-draft.md && \
grep -q "ideas.yaml" PROMPTS/skills/studio-draft.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

### Epic 5: Artifact System

#### US-014: Create Artifact Prompt
**As** Claude Code **I want to** have clear instructions in PROMPTS/40-artifacts.md **so that** I can generate working visualizations.

**Acceptance Criteria:**
- [ ] 40-artifacts.md explains three options: p5.js (creative/animated), D3.js (data-driven), Canvas (custom)
- [ ] 40-artifacts.md references BRAND/visuals/ for style templates
- [ ] 40-artifacts.md defines artifact file structure: artifacts/<name>/index.html, artifacts/<name>/sketch.js
- [ ] 40-artifacts.md states requirement: artifact must render without console errors before proposing
- [ ] 40-artifacts.md explains how to embed in MDX using iframe or component
- [ ] 40-artifacts.md defines graceful degradation: include static fallback image

**Verification:**
```bash
grep -q "p5.js" PROMPTS/40-artifacts.md && \
grep -q "D3" PROMPTS/40-artifacts.md && \
grep -q "Canvas" PROMPTS/40-artifacts.md && \
grep -q "visuals" PROMPTS/40-artifacts.md && \
grep -q "index.html" PROMPTS/40-artifacts.md && \
grep -q "console error" PROMPTS/40-artifacts.md && \
grep -q "MDX" PROMPTS/40-artifacts.md && \
grep -q "fallback" PROMPTS/40-artifacts.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-015: Create Artifact Testing Script
**As** Claude Code **I want to** run `scripts/test-artifact.sh <path>` **so that** I can verify visualizations work before proposing them.

**Acceptance Criteria:**
- [ ] scripts/test-artifact.sh exists and is executable (chmod +x)
- [ ] Script accepts a path argument to an HTML file
- [ ] Script uses Playwright to load the HTML file
- [ ] Script checks for console errors and returns exit code 1 if any found
- [ ] Script returns exit code 0 if no console errors
- [ ] Script outputs to stderr on failure
- [ ] Test fixtures exist: scripts/fixtures/good-artifact.html (no errors), scripts/fixtures/bad-artifact.html (has console.error)

**Verification:**
```bash
test -x scripts/test-artifact.sh && \
test -f scripts/fixtures/good-artifact.html && \
test -f scripts/fixtures/bad-artifact.html && \
scripts/test-artifact.sh scripts/fixtures/good-artifact.html && \
! scripts/test-artifact.sh scripts/fixtures/bad-artifact.html && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

#### US-016: Create Reusable Visualization Components
**As** Claude Code **I want to** have template components in BRAND/visuals/components/ **so that** I can scaffold visualizations quickly.

**Acceptance Criteria:**
- [ ] BRAND/visuals/components/p5-template.html exists with working p5.js setup
- [ ] BRAND/visuals/components/d3-template.html exists with working D3.js setup
- [ ] Each template includes usage instructions as HTML comments
- [ ] Each template uses colors from palette.md
- [ ] Templates pass artifact testing (no console errors)

**Verification:**
```bash
test -f BRAND/visuals/components/p5-template.html && \
test -f BRAND/visuals/components/d3-template.html && \
grep -q "usage" BRAND/visuals/components/p5-template.html && \
grep -q "usage" BRAND/visuals/components/d3-template.html && \
scripts/test-artifact.sh BRAND/visuals/components/p5-template.html && \
scripts/test-artifact.sh BRAND/visuals/components/d3-template.html && \
echo "PASS" || echo "FAIL"
```

**Priority:** P2

---

### Epic 6: Review System

#### US-017: Create Review Prompt
**As** Claude Code **I want to** have clear instructions in PROMPTS/50-review.md **so that** I can run quality checks.

**Acceptance Criteria:**
- [ ] 50-review.md defines checklist items: voice_consistency, technical_accuracy, artifacts_work, has_hook, brand_pillars
- [ ] 50-review.md explains voice_consistency: compare against BRAND/voice.md examples
- [ ] 50-review.md explains technical_accuracy: verify claims with sources, run code if present
- [ ] 50-review.md explains artifacts_work: run test-artifact.sh, verify no console errors
- [ ] 50-review.md explains how to write review/checklist.md with [x] or [ ] marks
- [ ] 50-review.md explains how to write review/edits.md with suggestions (never modify draft.md directly)
- [ ] 50-review.md states: if any check fails, do not proceed to publish

**Verification:**
```bash
grep -q "voice_consistency" PROMPTS/50-review.md && \
grep -q "technical_accuracy" PROMPTS/50-review.md && \
grep -q "artifacts_work" PROMPTS/50-review.md && \
grep -q "has_hook" PROMPTS/50-review.md && \
grep -q "checklist.md" PROMPTS/50-review.md && \
grep -q "edits.md" PROMPTS/50-review.md && \
grep -q "never modify draft" PROMPTS/50-review.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-018: Create Studio-Review Skill
**As a** content creator **I want to** run `/studio-review <slug>` to check a draft **so that** I catch issues before publishing.

**Acceptance Criteria:**
- [ ] Skill definition exists in PROMPTS/skills/studio-review.md
- [ ] Skill references reading the project's draft.md
- [ ] Skill references running artifact tests via test-artifact.sh
- [ ] Skill references creating/updating review/checklist.md
- [ ] Skill references creating review/edits.md for suggestions
- [ ] Skill explicitly states: do NOT modify draft.md

**Verification:**
```bash
test -f PROMPTS/skills/studio-review.md && \
grep -q "draft.md" PROMPTS/skills/studio-review.md && \
grep -q "test-artifact" PROMPTS/skills/studio-review.md && \
grep -q "checklist.md" PROMPTS/skills/studio-review.md && \
grep -q "edits.md" PROMPTS/skills/studio-review.md && \
grep -qE "(NOT|never|do not).*(modify|edit|change).*draft" PROMPTS/skills/studio-review.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

### Epic 7: Repurpose & Publish

#### US-019: Create Repurpose Prompt
**As** Claude Code **I want to** have clear instructions in PROMPTS/60-repurpose.md **so that** I can generate platform variants.

**Acceptance Criteria:**
- [ ] 60-repurpose.md explains LinkedIn format: professional tone, 1300 character limit, no more than 3 hashtags
- [ ] 60-repurpose.md shows structure: hook (first line), key insight, call to action
- [ ] 60-repurpose.md explains how to extract key points from draft.md
- [ ] 60-repurpose.md specifies output location: platforms/linkedin.md
- [ ] 60-repurpose.md includes example LinkedIn post

**Verification:**
```bash
grep -q "LinkedIn" PROMPTS/60-repurpose.md && \
grep -q "1300" PROMPTS/60-repurpose.md && \
grep -q "hashtag" PROMPTS/60-repurpose.md && \
grep -q "hook" PROMPTS/60-repurpose.md && \
grep -q "platforms/" PROMPTS/60-repurpose.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

#### US-020: Create Publish Prompt
**As** Claude Code **I want to** have clear instructions in PROMPTS/70-publish.md **so that** I can move content to the site.

**Acceptance Criteria:**
- [ ] 70-publish.md explains pre-check: verify review/checklist.md has all items passing
- [ ] 70-publish.md explains file move: draft.md → SITE/src/content/blog/<slug>.mdx
- [ ] 70-publish.md defines required MDX frontmatter: title, description, pubDate, tags, lane
- [ ] 70-publish.md explains artifact copy: artifacts/* → SITE/public/artifacts/<slug>/
- [ ] 70-publish.md explains status update: set idea status to "published" in ideas.yaml
- [ ] 70-publish.md explains build verification: run npm build, check for errors
- [ ] 70-publish.md explains error handling if build fails

**Verification:**
```bash
grep -q "checklist.md" PROMPTS/70-publish.md && \
grep -q "SITE/src/content/blog" PROMPTS/70-publish.md && \
grep -q "frontmatter" PROMPTS/70-publish.md && \
grep -q "title" PROMPTS/70-publish.md && \
grep -q "pubDate" PROMPTS/70-publish.md && \
grep -q "artifacts" PROMPTS/70-publish.md && \
grep -q "published" PROMPTS/70-publish.md && \
grep -q "error" PROMPTS/70-publish.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

#### US-021: Create Studio-Publish Skill
**As a** content creator **I want to** run `/studio-publish <slug>` to publish a post **so that** content goes live with minimal friction.

**Acceptance Criteria:**
- [ ] Skill definition exists in PROMPTS/skills/studio-publish.md
- [ ] Skill references verifying review checklist passed (all items [x])
- [ ] Skill references moving files to SITE/
- [ ] Skill references running npm build in SITE/
- [ ] Skill references updating idea status to "published"
- [ ] Skill references starting preview server and outputting localhost URL
- [ ] Skill references error handling: if any step fails, report and stop

**Verification:**
```bash
test -f PROMPTS/skills/studio-publish.md && \
grep -q "checklist" PROMPTS/skills/studio-publish.md && \
grep -q "SITE" PROMPTS/skills/studio-publish.md && \
grep -q "npm" PROMPTS/skills/studio-publish.md && \
grep -q "published" PROMPTS/skills/studio-publish.md && \
grep -q "localhost" PROMPTS/skills/studio-publish.md && \
grep -qE "error|fail" PROMPTS/skills/studio-publish.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

### Epic 8: System Integration

#### US-022: Create System Prompt
**As** Claude Code **I want to** read core operating rules from PROMPTS/00-system.md **so that** I follow the right patterns in every session.

**Acceptance Criteria:**
- [ ] 00-system.md states rule: "Read BRAND folder before any generation"
- [ ] 00-system.md states rule: "Never overwrite Mason's edits - suggestions go in review/edits.md"
- [ ] 00-system.md states rule: "Prefer presenting options over asking open-ended questions"
- [ ] 00-system.md states rule: "Test artifacts before proposing - must have no console errors"
- [ ] 00-system.md explains session design: incremental progress in 15-30 min sessions
- [ ] 00-system.md explains state persistence: progress saved in project folders between sessions

**Verification:**
```bash
grep -q "Read BRAND" PROMPTS/00-system.md && \
grep -q "Never overwrite" PROMPTS/00-system.md && \
grep -q "options" PROMPTS/00-system.md && \
grep -q "Test artifacts" PROMPTS/00-system.md && \
grep -q "15-30" PROMPTS/00-system.md && \
grep -q "session" PROMPTS/00-system.md && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-023: Create Makefile with Common Commands
**As a** content creator **I want to** run common operations via Make **so that** commands are discoverable and consistent.

**Acceptance Criteria:**
- [ ] `make help` target exists and lists all available commands
- [ ] `make setup` target exists (runs scripts/setup-skills.sh, npm install in SITE/, npx playwright install)
- [ ] `make preview` target exists (starts Astro dev server in SITE/)
- [ ] `make build` target exists (builds site in SITE/)
- [ ] `make deploy` target exists (runs `git push origin main` to trigger GitHub Actions)
- [ ] `make test` target exists (discovers and tests all artifacts via `find PROJECTS/*/artifacts -name "*.html"`)
- [ ] `make validate` target exists (validates YAML using Python with PyYAML)

**Verification:**
```bash
grep -q "help:" Makefile && \
grep -q "setup:" Makefile && \
grep -q "preview:" Makefile && \
grep -q "build:" Makefile && \
grep -q "deploy:" Makefile && \
grep -q "test:" Makefile && \
grep -q "validate:" Makefile && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

#### US-024: End-to-End Test with Example Post
**As a** content creator **I want to** have one complete example post **so that** I can verify the entire workflow works.

**Acceptance Criteria:**
- [ ] PROJECTS/example-post/ directory exists
- [ ] PROJECTS/example-post/brief.md exists with Scope, Audience, Key Points sections
- [ ] PROJECTS/example-post/outline.md exists with Hook, Sections, Takeaway
- [ ] PROJECTS/example-post/draft.md exists with complete post content
- [ ] PROJECTS/example-post/artifacts/ contains at least one working visualization
- [ ] PROJECTS/example-post/review/checklist.md exists with all items marked [x]
- [ ] SITE/src/content/blog/example-post.mdx exists with valid frontmatter
- [ ] Site builds successfully and contains example-post route

**Verification:**
```bash
test -d PROJECTS/example-post && \
test -f PROJECTS/example-post/brief.md && \
grep -q "Scope" PROJECTS/example-post/brief.md && \
test -f PROJECTS/example-post/outline.md && \
test -f PROJECTS/example-post/draft.md && \
test -d PROJECTS/example-post/artifacts && \
find PROJECTS/example-post/artifacts -name "index.html" | head -1 | xargs test -f && \
test -f PROJECTS/example-post/review/checklist.md && \
grep -q "\[x\]" PROJECTS/example-post/review/checklist.md && \
! grep -q "\[ \]" PROJECTS/example-post/review/checklist.md && \
test -f SITE/src/content/blog/example-post.mdx && \
grep -q "title:" SITE/src/content/blog/example-post.mdx && \
cd SITE && npm run build && \
test -d dist/blog/example-post && \
echo "PASS" || echo "FAIL"
```

**Priority:** P0

---

#### US-025: Create Skills Setup Script
**As a** content creator **I want to** run `scripts/setup-skills.sh` to install skills **so that** the repo is portable to new machines.

**Acceptance Criteria:**
- [ ] scripts/setup-skills.sh exists and is executable
- [ ] Script creates ~/.claude/commands/ directory if it doesn't exist
- [ ] Script symlinks all PROMPTS/skills/*.md files to ~/.claude/commands/
- [ ] Script outputs list of installed skills
- [ ] Running script twice is idempotent (doesn't error)

**Verification:**
```bash
test -x scripts/setup-skills.sh && \
scripts/setup-skills.sh && \
test -L ~/.claude/commands/studio-ideate.md && \
test -L ~/.claude/commands/studio-draft.md && \
test -L ~/.claude/commands/studio-review.md && \
test -L ~/.claude/commands/studio-publish.md && \
scripts/setup-skills.sh && \
echo "PASS" || echo "FAIL"
```

**Priority:** P1

---

## Schema Definitions

### ideas.yaml Schema

```yaml
# Each idea is an object with these required fields:
- id: string          # unique slug, e.g., "rimworld-agents-intro"
  title: string       # human-readable title
  lane: string        # one of: enterprise-ai, tribal-ai, deep-dive, experiments
  effort: string      # one of: small, medium, large
  hook: string        # one-sentence why-should-anyone-care
  audience: string    # who is this for
  artifacts: list     # list of required artifact types, e.g., ["p5-simulation", "d3-chart"]
  status: string      # one of: proposed, selected, in-progress, published
  created: string     # ISO date, e.g., "2024-01-15"
  series: string      # optional, series ID if part of multi-part
  notes: string       # optional, additional context
```

### series.yaml Schema

```yaml
# Each series is an object:
- id: string          # unique slug, e.g., "rimworld-agents"
  title: string       # series title
  north_star: string  # what's the overall goal of this series
  posts: list         # ordered list of idea IDs in the series
  terminology: object # key terms to use consistently
  status: string      # one of: planned, in-progress, complete
```

### Blog Post Frontmatter (MDX)

```yaml
---
title: string         # post title
description: string   # 1-2 sentence summary for SEO/preview
pubDate: string       # ISO date
updatedDate: string   # optional, ISO date
tags: list            # list of tags
lane: string          # content lane
series: string        # optional, series ID
heroImage: string     # optional, path to hero image
---
```

---

## Non-Functional Requirements

### Performance
- Astro build completes in < 60 seconds for up to 100 posts
- Local preview server starts in < 10 seconds
- Artifact tests complete in < 15 seconds per artifact

### Reliability
- All artifacts must render without console errors in Chromium (Playwright default)
- Interactive artifacts must include static fallback image for graceful degradation
- GitHub Actions deployment must complete without manual intervention when triggered

### Accessibility
- All images must have alt text
- Color contrast must meet WCAG AA standards (4.5:1 for text) - verified via manual review
- Site must be navigable with keyboard

### Usability
- Claude Code can navigate folder structure without confusion
- All prompts are self-contained within the repo
- Skills work reliably in 15-30 minute sessions

### Maintainability
- All brand guidelines in plain markdown
- YAML files validate against documented schemas
- Git history preserves all changes

---

## Success Metrics

1. **Cadence:** Publish thoughtful content every other week (26 posts/year)
2. **Quality:** Every post passes review checklist on first or second attempt
3. **Efficiency:** Time from idea selection to published post < 4 hours of work
4. **Reach:** LinkedIn posts generate engagement (comments, shares)
5. **Outcomes:** Speaking inquiries within 6 months of consistent publishing

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Visualization testing is flaky | Medium | Use Playwright with deterministic tests; accept manual verification as fallback |
| Voice guidelines are too vague | High | Include many concrete examples; iterate based on actual generated content |
| Astro migration breaks existing content | High | Keep Jekyll repo as backup; validate content counts during migration |
| Claude Code can't reliably read brand context | High | Structure prompts to explicitly list files; skills read BRAND/* first |
| 15-30 min sessions aren't enough | Medium | Design for smaller increments; skills save state in project folders |
| Artifact test script requires Playwright | Medium | Document Playwright install in README; make test target installs if missing |

---

## Dependencies & Setup

The following must be installed for the system to work:

1. **Node.js 18+** - for Astro
2. **Python 3.8+** - for YAML validation scripts
3. **PyYAML** - `pip install pyyaml`
4. **Playwright** - `npx playwright install chromium`

These are installed automatically via `make setup`.

---

## Open Questions

1. **Visual examples:** How should example screenshots be stored? (Propose: BRAND/examples/<name>.png with notes.md)
2. **Series.yaml:** Do we need to track post dependencies or just ordering?
3. **Interactive artifact testing:** For visualizations requiring clicks, accept manual verification with documented steps?
4. **Concurrent edits:** If two sessions edit ideas.yaml simultaneously, use git merge conflict resolution?
