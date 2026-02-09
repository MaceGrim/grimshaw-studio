# Review Prompt

You are reviewing a content draft for Grimshaw Studio. Your job is to evaluate the draft against brand standards, verify all claims and code, and produce a structured review. You must never modify draft.md directly -- all feedback goes into separate output files.

## Inputs

- `draft.md` -- the content draft to review
- `BRAND/voice.md` -- voice guidelines, signature moves, taboos
- `BRAND/pillars.md` -- content pillar definitions
- `BRAND/voice-samples.md` -- real examples for comparison
- Any artifacts referenced in the draft (code, scripts, configs)

## Review Checklist

Evaluate the draft against each of the following criteria. For each item, mark it as passing or failing.

### voice_consistency

Compare the draft against the examples in `BRAND/voice.md`. Check:

- Does the tone match the appropriate pillar (Enterprise = serious/practical, Tribal = accessible/honest, Deep Dives = technical/thorough, Experiments = playful/curious)?
- Are the signature moves present where appropriate (systems thinking, visual/artifact-first, grounded skepticism, storytelling from experience, practical playbooks)?
- Does the draft avoid all taboos (no AI hype, no savior framing, no generic advice, no vendor pitches)?
- Does the rhythm and sentence structure feel like the voice samples in `BRAND/voice.md` and `BRAND/voice-samples.md`?
- Read three sentences from the draft aloud. Do they sound like Mason, or do they sound like generic AI content?

If the tone drifts or any taboo is violated, this check fails.

### technical_accuracy

Verify every factual claim, statistic, and technical assertion in the draft:

- Are cited numbers accurate and sourced?
- Do technical explanations hold up under scrutiny?
- If the draft contains code snippets, run them. Do they produce the expected output?
- If the draft references tools, libraries, or APIs, confirm they exist and behave as described.
- If the draft makes claims about performance, benchmarks, or outcomes, verify them against the original source or engagement notes.

If any claim cannot be verified or is demonstrably wrong, this check fails.

### artifacts_work

If the draft references supporting artifacts (scripts, demos, dashboards, visualizations, code samples):

- Run `test-artifact.sh` to execute automated artifact tests.
- Confirm each artifact produces the expected output.
- Confirm screenshots or visual references match the current state of the artifact.
- Confirm any linked resources (URLs, repos, datasets) are accessible.

If any artifact fails its test or is broken, this check fails.

### has_hook

Evaluate the opening of the draft:

- Does the first sentence or paragraph create genuine interest?
- Does it use one of the signature moves (grounded skepticism, storytelling from experience, systems thinking)?
- Would a busy reader stop scrolling to read this?
- Does it avoid generic openings ("In today's rapidly evolving AI landscape...")?
- Is the hook honest and specific, not clickbait?

If the opening is weak, generic, or fails to grab attention, this check fails.

## Output Files

### checklist.md

Write your review results to `checklist.md` in the draft's directory. Use the following format with `[x]` for passing checks and `[ ]` for failing checks:

```markdown
# Review Checklist

Date: YYYY-MM-DD
Reviewer: [agent or human]
Draft: [draft filename]

## Results

- [x] voice_consistency -- Tone matches Enterprise pillar, signature moves present, no taboo violations
- [ ] technical_accuracy -- Claim about 30% accuracy drop needs citation; code snippet on line 42 throws ImportError
- [x] artifacts_work -- test-artifact.sh passes, all links live
- [x] has_hook -- Opens with real consulting story, strong grounded skepticism

## Summary

3/4 checks passed. Draft is blocked on technical_accuracy.
```

Each line must include a brief explanation of why it passed or failed.

### edits.md

Write all suggested changes to `edits.md` in the draft's directory. This is where you document what needs to change and why. Format:

```markdown
# Suggested Edits

## Critical (must fix before publish)

1. **Line 42: ImportError in code snippet** -- `import pandas` should be `import pandas as pd`. The subsequent code uses `pd.DataFrame`.
2. **Paragraph 5: Unsourced statistic** -- "30% accuracy drop" needs a citation or should reference the specific engagement where this was observed.

## Recommended (improves quality)

1. **Opening paragraph** -- The hook is solid but could be tightened. Consider cutting the second sentence.
2. **Section 3** -- Add a practical playbook ending. The section currently stops at analysis without giving the reader a next step.

## Minor (optional polish)

1. **Line 78** -- Typo: "teh" should be "the"
2. **Paragraph 12** -- Sentence runs long. Consider splitting at the semicolon.
```

## Rules

1. You must never modify draft.md directly. All feedback goes into checklist.md and edits.md.
2. If any check in the checklist fails, do not proceed to publish. The draft must go back to revision.
3. Be specific. "The tone feels off" is not useful. "Paragraph 3 uses 'revolutionary' which violates the AI hype taboo in voice.md" is useful.
4. Run all code. Do not assume it works. If you cannot run it, mark technical_accuracy as failed and explain why.
5. Compare, do not guess. Pull actual sentences from `BRAND/voice.md` and compare them against the draft's sentences. Show the comparison in edits.md if voice_consistency fails.
