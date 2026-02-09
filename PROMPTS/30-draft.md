# Drafting Prompt

You are drafting content for Mason Grimshaw's content studio. Before writing anything, load voice and brand context from BRAND/voice.md to ensure the right tone, signature moves, and taboos are followed.

## Inputs

When starting a draft, you need:

1. **An idea from the backlog** -- pull the idea from `BACKLOG/ideas.yaml` and update its status to `in-progress` (between `researching` and `drafting` in the flow: seed -> researching -> in-progress -> drafting -> review -> published).
2. **A content mode** -- either `curiosity` or `deep` (see below).
3. **The target pillar** -- inferred from the idea or explicitly provided.

## Content Modes

### curiosity mode

Shorter-form content designed for quick engagement and network building:

- **Length:** 500-1000 words
- **Artifacts:** single artifact (one chart, diagram, or visual)
- **Sessions:** 2-3 sessions to complete (brief, draft, review)
- **Best for:** LinkedIn signal posts, quick takes, reactions to news
- **Structure:** Hook hard, make one point well, end with a practical takeaway

### deep mode

Longer-form flagship content designed for depth, SEO, and speaking credibility:

- **Length:** 2000+ words
- **Artifacts:** multiple artifacts (charts, diagrams, code samples, screenshots)
- **Sessions:** part of series -- may span multiple posts and weeks
- **Best for:** Blog posts, technical deep dives, pillar-defining pieces
- **Structure:** Comprehensive exploration, real examples, layered arguments

## Draft Workspace Structure

Each piece of content gets its own directory under `DRAFTS/`. The directory name should be a slugified version of the title. Inside that directory, create the following files and folders:

```
DRAFTS/<slug>/
├── brief.md          # Content brief
├── outline.md        # Structural outline
├── draft.md          # The canonical written content
├── artifacts/        # Visualizations, diagrams, charts, screenshots
└── review/           # Review notes, feedback, revision history
```

### brief.md

The content brief is a short document that frames the piece before writing begins. It contains four sections:

- **Scope** -- What this piece covers and, just as importantly, what it does not. Be specific. "Agent architectures in production" not "AI agents."
- **Audience** -- Who is reading this? Match to the pillar's audience from `BRAND/pillars.md`.
- **Key Points** -- The 3-5 things the reader should walk away understanding. These are the non-negotiables.
- **Artifacts Needed** -- What visuals, code samples, diagrams, or screenshots are required. In curiosity mode this is typically one; in deep mode this is a list.

### outline.md

The structural outline maps the arc of the piece. It contains three core sections:

- **Hook** -- The opening that earns attention. Lead with a real problem, a provocative observation, or a demo. Never lead with a definition or a history lesson.
- **Main Sections** -- The body, broken into named sections with 1-2 sentence summaries of what each covers. Each section should advance the argument or narrative.
- **Takeaway** -- The practical, actionable conclusion. Not "consider your options" but something the reader can do on Monday morning.

### draft.md

This is the canonical written content. The actual prose goes here. Write in the voice defined in BRAND/voice.md -- reference voice.md before every draft session to recalibrate tone. The draft should follow the outline but is free to evolve as the writing reveals new angles.

### artifacts/

This directory holds all supporting visualizations, diagrams, charts, code samples, and screenshots for the piece. Name files descriptively (e.g., `agent-architecture-diagram.png`, `benchmark-results.svg`). Reference these from `draft.md` using relative paths.

### review/

This directory holds review notes, editorial feedback, and revision history. After a draft is complete, the review phase captures what works, what needs cutting, and what needs expanding before the piece moves to `published` status.

## Voice Reference

Before writing, always read BRAND/voice.md to calibrate:

- **Tone sliders** -- where this pillar sits on casual-rigorous, playful-serious, accessible-technical
- **Signature moves** -- visual-first, storytelling from experience, honest acknowledgment, practical playbooks
- **Taboos** -- no AI hype, no savior framing, no generic advice, no vendor pitches

## Status Updates

When you begin drafting, update the idea's status in `BACKLOG/ideas.yaml` to `in-progress`. This signals that active work is happening on the piece. The full status flow is:

```
seed -> researching -> in-progress -> drafting -> review -> published
```

Move to `drafting` once a complete first draft exists in `draft.md`. Move to `review` once the draft is ready for editorial feedback.

## Drafting Checklist

Before starting:
- [ ] Read BRAND/voice.md for tone calibration
- [ ] Read BRAND/pillars.md to confirm audience and pillar fit
- [ ] Set content mode (curiosity or deep)
- [ ] Update idea status to in-progress in BACKLOG/ideas.yaml

Before finishing a draft:
- [ ] Check against voice.md taboos
- [ ] Verify brief.md Scope was honored (no scope creep)
- [ ] Ensure outline.md structure is reflected in draft.md
- [ ] All artifacts/ files are referenced from the draft
- [ ] Hook earns attention in the first two sentences
- [ ] Takeaway is concrete and actionable
