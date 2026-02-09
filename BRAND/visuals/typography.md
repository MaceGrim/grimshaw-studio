# Typography

Type choices for Grimshaw Studio. The goal: authoritative without being corporate, readable without being bland.

---

## Font Families

### Heading Font: Inter
- **Weight:** 700 (Bold) for H1, 600 (Semi-Bold) for H2-H3
- **Why Inter:** Clean geometric sans-serif with strong presence at large sizes. Designed for screens, excellent at every weight, free and open-source. Avoids the overused Montserrat/Poppins territory while staying modern. The slightly tighter letter-spacing at bold weights gives headings a punchy, confident feel that matches the brand voice.
- **Fallback stack:** `'Inter', 'Helvetica Neue', Arial, sans-serif`

### Body Font: Source Serif 4
- **Weight:** 400 (Regular) for body, 600 (Semi-Bold) for inline emphasis
- **Why Source Serif 4:** A contemporary serif with excellent readability at body sizes. The slight warmth of a serif pairs well with the cream background and signals "this is worth reading carefully." Designed by Adobe for extended reading on screens -- generous x-height, open counters, clear distinction between letterforms. Free and open-source.
- **Fallback stack:** `'Source Serif 4', 'Georgia', 'Times New Roman', serif`

### Monospace Font: JetBrains Mono
- **Weight:** 400 (Regular), 700 (Bold) for syntax highlights
- **Why JetBrains Mono:** Purpose-built for code. Ligatures available but optional. Distinguishes between similar characters (0/O, 1/l/I) cleanly. Feels technical without being sterile.
- **Fallback stack:** `'JetBrains Mono', 'Fira Code', 'Consolas', monospace`

---

## Size Hierarchy

All sizes in `rem` for consistent scaling. Base size: `1rem = 16px`.

| Element | Size | Line Height | Weight | Font | Letter Spacing |
|---------|------|-------------|--------|------|----------------|
| H1 | 2.5rem (40px) | 1.2 | 700 | Inter | -0.02em |
| H2 | 1.75rem (28px) | 1.3 | 600 | Inter | -0.01em |
| H3 | 1.25rem (20px) | 1.4 | 600 | Inter | 0 |
| H4 | 1.1rem (17.6px) | 1.4 | 600 | Inter | 0 |
| Body | 1.125rem (18px) | 1.7 | 400 | Source Serif 4 | 0 |
| Body small | 0.9rem (14.4px) | 1.6 | 400 | Source Serif 4 | 0 |
| Caption | 0.8rem (12.8px) | 1.5 | 400 | Inter | 0.02em |
| Code block | 0.9rem (14.4px) | 1.6 | 400 | JetBrains Mono | 0 |
| Inline code | 0.85rem (13.6px) | inherit | 400 | JetBrains Mono | 0 |
| Nav link | 0.95rem (15.2px) | 1.4 | 600 | Inter | 0.03em |
| Button | 1rem (16px) | 1.4 | 600 | Inter | 0.01em |

---

## Spacing Rules

### Paragraph Spacing
- Between paragraphs: `1.5rem`
- After headings: `0.75rem` (pull content close to its heading)
- Before headings: `2.5rem` (clear separation from previous section)

### Heading Stacking
When H2 follows H1 (or H3 follows H2) without body text between them, collapse the gap:
- H1 then H2: `1rem` gap
- H2 then H3: `0.75rem` gap

### Maximum Line Length
- Body text: 65-75 characters per line (~640px at body size)
- Headings: no max, but break naturally at ~900px

---

## Typography by Visual Mode

Each visual mode (defined in palette.md) adjusts type presentation. The three modes are playful, technical, and minimal.

### Playful Mode Typography
- Body size bumps to `1.2rem` (19.2px) for a friendlier feel
- H1 can go up to `3rem` (48px) for impact
- Line height stays at 1.7 for body readability
- Captions can use Inter instead of Source Serif 4 for a casual tone
- Inline code gets slightly rounded background (per palette)

### Technical Mode Typography
- Body stays at `1.125rem` (18px) -- standard, no embellishment
- Code blocks get priority: larger at `1rem` (16px) with `1.7` line height
- Tables use `body small` sizing (0.9rem) for density
- H1 drops to `2rem` (32px) to save vertical space for content
- Tighter paragraph spacing: `1.25rem` between paragraphs
- Numbered sections preferred (1.1, 1.2, etc.)

### Minimal Mode Typography
- Body bumps to `1.25rem` (20px) for a reading-optimized experience
- H1 at `2.5rem` (40px), nothing larger needed
- Line height increases to `1.8` for body text
- Max line length tightens to 60 characters (~600px)
- Generous margins: content centered in a narrow column
- Headings use Inter at weight 700 only -- no semi-bold, full bold everywhere
- Minimal use of code blocks; inline code only when unavoidable

---

## CSS Custom Properties

For implementation, define these as CSS custom properties:

```css
:root {
  /* Heading font */
  --font-heading: 'Inter', 'Helvetica Neue', Arial, sans-serif;

  /* Body font */
  --font-body: 'Source Serif 4', 'Georgia', 'Times New Roman', serif;

  /* Code font */
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;

  /* Size scale */
  --text-h1: 2.5rem;
  --text-h2: 1.75rem;
  --text-h3: 1.25rem;
  --text-h4: 1.1rem;
  --text-body: 1.125rem;
  --text-small: 0.9rem;
  --text-caption: 0.8rem;
  --text-code: 0.9rem;

  /* Line heights */
  --leading-tight: 1.2;
  --leading-snug: 1.3;
  --leading-normal: 1.4;
  --leading-relaxed: 1.7;

  /* Spacing */
  --space-paragraph: 1.5rem;
  --space-before-heading: 2.5rem;
  --space-after-heading: 0.75rem;
}
```

---

## Loading Strategy

1. **Inter and Source Serif 4** from Google Fonts with `display=swap` to prevent invisible text.
2. **JetBrains Mono** loaded only on pages with code blocks (conditional loading).
3. Subset fonts to Latin characters unless content requires extended character sets.
4. Preload the heading font (Inter Bold) since it appears above the fold on every page.

```html
<link rel="preload" href="/fonts/inter-bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@600;700&family=Source+Serif+4:wght@400;600&display=swap">
```
