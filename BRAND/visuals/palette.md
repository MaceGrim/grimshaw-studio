# Color Palette

The Grimshaw Studio palette is built around warmth, authority, and readability. Every color earns its place -- nothing decorative, nothing arbitrary.

---

## Core Colors

### Burnt Orange (Primary Accent)
- **Hex:** `#CC5500`
- **Usage:** Call-to-action buttons, inline links, highlighted terms, section dividers, pull quotes. This is the color that says "look here." Use it sparingly so it keeps its punch.
- **Avoid:** Large background fills (too intense), body text (low readability on light backgrounds).

### Dark Navy (Headers / Secondary)
- **Hex:** `#1B2A4A`
- **Usage:** H1 and H2 headings, navigation elements, footer backgrounds, code block frames, sidebar accents. Provides weight and authority without going full black.
- **Avoid:** Small body text on light backgrounds (use Warm Charcoal instead for better contrast at small sizes).

### Cream (Background)
- **Hex:** `#FFF8F0`
- **Usage:** Primary page background, card backgrounds, content area fill. Warmer than pure white, easier on the eyes during long reads. Pairs naturally with both the navy and orange.
- **Avoid:** Text color (invisible against white or light elements).

---

## Complementary Colors

### Warm Charcoal (Body Text)
- **Hex:** `#3D3D3D`
- **Usage:** All body text, captions, metadata, secondary labels. Softer than pure black (#000000), which feels harsh on cream backgrounds. High readability at all sizes.

### Light Navy (Hover / Interactive States)
- **Hex:** `#2E4A7A`
- **Usage:** Hover states on navy elements, active link indicators, secondary buttons, tag backgrounds. Provides a visible but subtle shift from Dark Navy for interactive feedback.

### Muted Sand (Borders / Dividers)
- **Hex:** `#E8DFD0`
- **Usage:** Horizontal rules, card borders, table lines, subtle section separators. Sits between Cream and Warm Charcoal without demanding attention.

### Deep Rust (Error / Emphasis)
- **Hex:** `#A04030`
- **Usage:** Error states, warning callouts, destructive action buttons. Close enough to Burnt Orange to feel on-brand, dark enough to signal urgency.

### Soft Sage (Success / Positive)
- **Hex:** `#5A7A60`
- **Usage:** Success indicators, positive callouts, completion states. A grounded green that avoids the neon-tech look.

---

## Color Combinations by Context

### Blog Posts / Long-Form Content
| Element | Color | Hex |
|---------|-------|-----|
| Background | Cream | `#FFF8F0` |
| Body text | Warm Charcoal | `#3D3D3D` |
| Headings | Dark Navy | `#1B2A4A` |
| Links | Burnt Orange | `#CC5500` |
| Link hover | Light Navy | `#2E4A7A` |
| Dividers | Muted Sand | `#E8DFD0` |

### Code / Technical Content
| Element | Color | Hex |
|---------|-------|-----|
| Code block background | Dark Navy | `#1B2A4A` |
| Code text | Cream | `#FFF8F0` |
| Inline code background | Muted Sand | `#E8DFD0` |
| Inline code text | Warm Charcoal | `#3D3D3D` |
| Syntax highlights | Burnt Orange | `#CC5500` |

### Cards / Components
| Element | Color | Hex |
|---------|-------|-----|
| Card background | Cream | `#FFF8F0` |
| Card border | Muted Sand | `#E8DFD0` |
| Card title | Dark Navy | `#1B2A4A` |
| Card CTA | Burnt Orange | `#CC5500` |

### Dark Sections (Footer, Hero)
| Element | Color | Hex |
|---------|-------|-----|
| Background | Dark Navy | `#1B2A4A` |
| Heading text | Cream | `#FFF8F0` |
| Body text | Muted Sand | `#E8DFD0` |
| Accent | Burnt Orange | `#CC5500` |

---

## Visual Modes

The studio publishes across four content pillars, and the visual presentation should shift to match. Three modes handle this:

### Playful Mode
**Mode ID:** `playful`
**Used for:** Experiments, fun projects, "let's find out" content, sports analytics, simulations.

| Property | Value |
|----------|-------|
| Primary accent | Burnt Orange `#CC5500` at full saturation |
| Background | Cream `#FFF8F0` |
| Headings | Dark Navy `#1B2A4A` |
| Animation | Allowed -- subtle transitions, hover effects, interactive elements |
| Imagery | Screenshots, GIFs, embedded demos, colorful diagrams |
| Layout | Looser grid, asymmetric elements OK, generous image sizing |
| Borders | Rounded corners (8px+), softer edges |
| Extra accent | Light Navy `#2E4A7A` for secondary interactive elements |

Playful mode is where personality shows. The palette stays the same but the *application* is bolder -- bigger accent splashes, animated transitions, more visual weight on demos and artifacts.

### Technical Mode
**Mode ID:** `technical`
**Used for:** Deep dives, data-heavy posts, multi-part series, architecture breakdowns.

| Property | Value |
|----------|-------|
| Primary accent | Burnt Orange `#CC5500` used only for key callouts |
| Background | Cream `#FFF8F0` |
| Headings | Dark Navy `#1B2A4A` |
| Animation | Minimal -- no decorative motion, functional transitions only |
| Imagery | Diagrams, architecture charts, code screenshots, data tables |
| Layout | Tight grid, consistent spacing, information-dense |
| Borders | Sharp corners (2px max radius), precise lines |
| Code blocks | Prominent, Dark Navy `#1B2A4A` background with Cream `#FFF8F0` text |
| Extra colors | Muted Sand `#E8DFD0` for table striping, Soft Sage `#5A7A60` for annotations |

Technical mode pulls back on decoration and pushes information density up. The palette is muted in practice -- Burnt Orange appears only at decision points (key findings, important warnings), never as decoration.

### Minimal Mode
**Mode ID:** `minimal`
**Used for:** Editorial pieces, opinion posts, Tribal AI perspectives, LinkedIn long-form.

| Property | Value |
|----------|-------|
| Primary accent | Burnt Orange `#CC5500` used for a single focal element per page |
| Background | Cream `#FFF8F0` |
| Headings | Dark Navy `#1B2A4A` |
| Animation | None |
| Imagery | One hero image max, otherwise text-only |
| Layout | Single column, generous whitespace, wide margins |
| Borders | None or hairline Muted Sand `#E8DFD0` only |
| Typography | Larger body text, more line height, reading-optimized |
| Max content width | 640px |

Minimal mode is about the words. The palette recedes almost entirely -- Dark Navy headings, Warm Charcoal text, Cream background, and one Burnt Orange accent (maybe a pull quote border or the author byline). Everything else is whitespace.

---

## Accessibility Notes

- Warm Charcoal `#3D3D3D` on Cream `#FFF8F0` passes WCAG AA for body text at all sizes.
- Dark Navy `#1B2A4A` on Cream `#FFF8F0` passes WCAG AAA for headings.
- Burnt Orange `#CC5500` on Cream `#FFF8F0` passes WCAG AA for large text (18px+). Do not use for small body text.
- Cream `#FFF8F0` on Dark Navy `#1B2A4A` passes WCAG AAA for inverted sections.
- Always test color combinations with a contrast checker before shipping.
