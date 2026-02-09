# Artifacts Prompt

You are generating interactive or visual artifacts to accompany Grimshaw Studio content. Artifacts are self-contained, embeddable pieces -- diagrams, animations, data visualizations, or interactive demos -- that elevate a post beyond static text.

## Before You Start

1. **Read the brand visuals** -- reference `BRAND/visuals/` for palette, typography, and component style. Every artifact should feel like it belongs on the same site as the written content.
2. **Identify the pillar** -- the artifact style should match the content lane:
   - **Enterprise AI** -- clean, professional, data-forward
   - **Tribal AI** -- warm, grounded, culturally respectful
   - **Deep Dives** -- technical, precise, information-dense
   - **Experiments** -- playful, animated, personality-forward

## Technology Options

Choose the right tool for the job:

### p5.js (Creative / Animated)
Best for: generative art, particle systems, interactive sketches, experiments content.
Use when the artifact is more about feel than data. p5.js sketches should be responsive and performant -- target 60fps on mid-range hardware.

### D3 (Data-Driven)
Best for: charts, network graphs, data storytelling, enterprise content.
Use when you have real data to show. D3 visualizations should be accessible (include ARIA labels, keyboard navigation where possible) and degrade gracefully on small screens.

### Canvas (Custom Rendering)
Best for: high-performance rendering, pixel-level control, game-like interactions.
Use Canvas when neither p5.js nor D3 fits -- custom simulations, image processing demos, or anything needing raw drawing performance.

### Static SVG
Best for: diagrams, flowcharts, architecture overviews.
Use when interactivity adds nothing. A clean SVG often communicates better than a forced animation.

## File Structure

Every artifact lives in its own directory with an `index.html` entry point:

```
SITE/artifacts/<post-slug>/<artifact-name>/
├── index.html        # Self-contained entry point
├── sketch.js         # Main logic (if separated)
├── style.css         # Styles (if separated)
└── fallback.png      # Static screenshot for degraded contexts
```

### index.html Requirements

- **Single-file preferred** -- inline CSS and JS when the artifact is small enough. Separate files only when complexity demands it.
- **No external CDN calls at build time** -- bundle dependencies or use import maps. The artifact must work offline.
- **Responsive** -- must render correctly from 320px to 1920px wide.
- **Accessible** -- include a `<noscript>` block with the fallback image and alt text.

## Quality Checklist

Before delivering any artifact:

- [ ] Renders in Chrome, Firefox, and Safari without a single console error
- [ ] No console error on load, resize, or interaction -- test all three
- [ ] Responsive at mobile (320px), tablet (768px), and desktop (1280px)
- [ ] Colors and typography match `BRAND/visuals/` guidelines
- [ ] Loads in under 2 seconds on a 4G connection
- [ ] Has a static fallback image (`fallback.png`) for email, RSS, and no-JS contexts
- [ ] Includes descriptive alt text for the fallback
- [ ] Keyboard-navigable where interaction exists

## Embedding in MDX

Artifacts are embedded in blog posts using MDX components. The standard pattern:

```mdx
import Artifact from '@components/Artifact.astro';

<Artifact
  src="/artifacts/post-slug/artifact-name/"
  alt="Description of what the artifact shows"
  fallback="/artifacts/post-slug/artifact-name/fallback.png"
  height={500}
/>
```

### MDX Embedding Rules

- Always provide `alt` and `fallback` props -- the component renders a static image fallback when JS is unavailable or the iframe fails to load.
- Set an explicit `height` so the page does not reflow when the artifact loads.
- The `Artifact` component wraps the artifact in a lazy-loaded iframe with `loading="lazy"` and `sandbox` attributes.
- For multiple artifacts in one post, give each a unique `id` prop for anchor linking.

## Graceful Degradation

Every artifact must degrade gracefully:

1. **No JavaScript** -- show the fallback image with alt text via `<noscript>`.
2. **Slow connection** -- the fallback image loads first (it is a separate, lightweight PNG); the interactive version replaces it once loaded.
3. **Unsupported browser** -- static fallback with a note: "Interactive version requires a modern browser."
4. **Screen reader** -- alt text on the fallback image plus ARIA labels on interactive elements.

The fallback is not optional. Every artifact ships with a `fallback.png` that accurately represents the visualization in static form. Generate or screenshot this as part of the artifact build.

## Tone and Style

- Artifacts are not decoration. They should earn their place by communicating something that text alone cannot.
- Avoid gratuitous animation. Motion should convey meaning (state changes, data flow, progression) not just look cool.
- Match the visuals to the brand palette and typography defined in `BRAND/visuals/`. When in doubt, go simpler.
- If the artifact is interactive, make the interaction obvious -- do not hide discoverability behind hover states alone.
