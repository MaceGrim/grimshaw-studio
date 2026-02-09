# Add Idea to Backlog

Quick-add a content idea to the backlog.

## Instructions

1. Parse the argument `$ARGUMENTS` as the idea topic/title

2. If no argument provided, ask: "What's the idea?"

3. Infer the pillar from the topic:
   - Enterprise AI: production systems, CTOs, implementation, agents in production
   - Tribal AI: Indigenous, sovereignty, tribal communities, capacity building
   - Deep Dives: technical series, from scratch, internals, architecture
   - Experiments: fun, visualization, games, simulations, sports, playful

4. Generate a hook (one compelling sentence that makes someone want to read it)

5. Read `BACKLOG/ideas.yaml` and append a new entry:
   ```yaml
   - title: "[The idea]"
     pillar: [inferred pillar]
     status: seed
     hook: "[Generated hook]"
     notes: ""
     added: [today's date YYYY-MM-DD]
   ```

6. Confirm what was added:
   ```
   Added to backlog:

   Title: [title]
   Pillar: [pillar]
   Hook: [hook]
   ```

7. Ask if they want to start drafting it now (offer to run /draft)
