# Draft Content

Start drafting a piece of content with full voice context loaded.

## Instructions

1. Parse `$ARGUMENTS` as either:
   - An idea title from the backlog
   - A new topic to draft (will be added to backlog first)

2. If it matches a backlog item, load that idea's details

3. **Load brand context** (read these files):
   - `BRAND/voice.md` - tone, signature moves, taboos
   - `BRAND/pillars.md` - understand the pillar this fits
   - `BRAND/voice-samples.md` - find samples matching this pillar

4. Determine the pillar and set tone:
   - Enterprise = serious, practical, grounded
   - Tribal = accessible, honest, Indigenous-led
   - Deep Dives = technical, thorough
   - Experiments = playful, curious

5. Ask clarifying questions:
   - What's the main point you want to make?
   - Any specific examples or stories to include?
   - Target length? (LinkedIn post, blog post, long-form)
   - Any visual/artifact to lead with?

6. Create draft file at `DRAFTS/[slugified-title].md` with frontmatter:
   ```markdown
   ---
   title: "[Title]"
   pillar: [pillar]
   status: drafting
   created: [date]
   ---

   [Draft content here]
   ```

7. Write the first draft, matching voice samples for rhythm and tone

8. After drafting, offer:
   - Review against taboos
   - Refine specific sections
   - Update backlog status to "drafting"

9. Update `BACKLOG/ideas.yaml` status to `drafting`
