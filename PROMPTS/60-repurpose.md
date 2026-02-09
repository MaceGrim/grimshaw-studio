# Repurpose Prompt

Adapt flagship blog content for distribution across social platforms. Each platform has different constraints, audiences, and norms. This prompt focuses on LinkedIn as the primary repurpose target.

---

## Step 1: Load Source Content

Read the completed blog post from its project folder:

1. `draft.md` — The published blog content
2. `brief.md` — Original scope and key points
3. `BRAND/voice.md` — Tone calibration for the target platform

---

## Step 2: LinkedIn Adaptation

LinkedIn is the primary signal platform for Grimshaw Studio. Repurposed posts go in the project's `platforms/` directory.

### Format Constraints

- **Maximum length:** 1300 characters for the visible portion (before "see more"). The full post can be longer, but the hook must land in the first 1300 characters.
- **Structure:** Open with a strong hook that creates tension or curiosity. Use short paragraphs (1-3 sentences). Break up the text with line spacing.
- **Hashtags:** Include 3-5 relevant hashtag tags at the end of the post. Use a mix of broad reach tags (`#AI`, `#MachineLearning`) and niche tags (`#TribalTech`, `#AIInProduction`). Do not embed hashtags mid-sentence.

### Hook Strategy

The hook is the single most important element. It must:

- Create immediate tension, curiosity, or recognition
- Be specific, not generic ("We deployed an AI agent to production and it worked for exactly 3 days" not "AI agents are hard")
- Use one of Mason's signature moves: grounded skepticism, storytelling from experience, or a surprising data point
- Land in the first 2-3 lines (what shows before "see more")

### Adaptation Rules

- **Distill, don't summarize.** Extract the single most compelling insight from the blog post and build the LinkedIn post around it. Do not try to compress 2000 words into 400.
- **Add a personal angle.** LinkedIn rewards first-person experience. Frame the insight through Mason's direct experience.
- **End with engagement.** Close with a question, a challenge, or a concrete takeaway that invites response.
- **Maintain voice.** The LinkedIn version must still sound like Mason. Re-read `BRAND/voice.md` before adapting.

### Output

Save the LinkedIn adaptation to `platforms/linkedin.md` in the project folder.

---

## Step 3: Platform-Specific Adjustments

When repurposing for additional platforms beyond LinkedIn, create separate files in `platforms/`:

- `platforms/linkedin.md` — LinkedIn post
- `platforms/twitter-thread.md` — Twitter/X thread (if applicable)
- `platforms/newsletter.md` — Newsletter excerpt (if applicable)

Each platform file should be self-contained and ready to copy-paste into the platform.

---

## Repurpose Checklist

- [ ] Source blog post read and key insight identified
- [ ] LinkedIn post opens with a strong hook
- [ ] Post fits within 1300 character visible limit for the hook portion
- [ ] 3-5 hashtag tags included at the end
- [ ] Voice matches BRAND/voice.md
- [ ] Saved to platforms/ directory
- [ ] No AI hype, savior framing, or generic advice
