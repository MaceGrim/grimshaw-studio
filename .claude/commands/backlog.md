# View Content Backlog

Display and filter ideas from the backlog.

## Instructions

1. Read `BACKLOG/ideas.yaml`

2. Parse optional filter from `$ARGUMENTS`:
   - `enterprise` - show only Enterprise AI ideas
   - `tribal` - show only Tribal AI ideas
   - `deep-dive` - show only Deep Dive ideas
   - `experiments` - show only Experiments ideas
   - `seed` / `drafting` / `review` - filter by status
   - No argument = show all

3. Display ideas in a clean format:

   ```
   # Content Backlog

   ## Enterprise AI (3 ideas)

   1. **The Trusted Performer Test** [seed]
      Hook: Put AI outputs alongside your best people...

   2. **Prototype to Production** [seed]
      Hook: The demo worked. Now what?

   ## Tribal AI (2 ideas)
   ...
   ```

4. Show summary at the end:
   ```
   ---
   Total: X ideas (Y seed, Z drafting, W review)

   To draft an idea: /draft "Title"
   To add an idea: /idea "topic"
   ```

5. If a specific idea is requested by name, show full details including notes
