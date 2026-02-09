# Publish Prompt

Instructions for the final publishing workflow — moving approved content from the project folder to the live Astro site.

---

## Prerequisites

Before publishing, confirm:

1. **Review passed** — Read `checklist.md` in the project's review/ directory. All checks must be `[x]`. If any check is failing, return to the review/revision phase. Do not publish content with unresolved issues.
2. **Edits applied** — All critical items from `edits.md` have been addressed in the draft.

---

## Step 1: Prepare Frontmatter

Create the Astro-compatible frontmatter block for the blog post. Every published post requires:

```yaml
---
title: "The Post Title"
description: "A one-sentence summary for SEO and social sharing"
pubDate: 2026-01-15
updatedDate: 2026-01-15
pillar: "enterprise"
tags: ["ai", "production"]
heroImage: "/blog/<slug>/hero.png"
draft: false
---
```

### Required Fields

- **title** — The post title, matching the draft
- **description** — One sentence for meta tags and social cards
- **pubDate** — The publication date in YYYY-MM-DD format
- **pillar** — One of: `enterprise`, `tribal`, `deep-dive`, `experiments`
- **tags** — Array of relevant tags for categorization and search

### Optional Fields

- **updatedDate** — Set when a published post is later revised
- **heroImage** — Path to the hero image if one exists
- **draft** — Set to `false` for published posts; `true` to hide from production

---

## Step 2: Copy to Site

Move the approved content into the Astro site:

1. Create the blog post file at `SITE/src/content/blog/<slug>.md`
2. Add the frontmatter block at the top
3. Copy the draft body content below the frontmatter
4. Copy all artifacts (images, diagrams, code samples) to `SITE/public/blog/<slug>/`
5. Update image and asset references in the post to use correct public paths

---

## Step 3: Verify Locally

Build and preview the site locally to catch errors before deploying:

```bash
cd SITE
npm install
npm run dev
```

Check the published post at the local dev URL:

- Does the title render correctly?
- Do all images and artifacts load?
- Are code blocks syntax-highlighted?
- Is the layout consistent with other posts?
- Does the post appear in the blog index?

If any element is broken or missing, fix the error before proceeding.

---

## Step 4: Production Build

Run a production build to catch errors the dev server might miss:

```bash
cd SITE
npm run build
```

If the build fails, diagnose the error. Common issues:

- Frontmatter schema mismatch (missing required fields)
- Broken image references
- TypeScript type errors in content collections

Do not deploy a broken build. Fix the error and rebuild.

---

## Step 5: Update Status

After the post is verified and builds cleanly:

1. Update the idea's status in `BACKLOG/ideas.yaml` to `published`
2. Add the publication date and URL to the idea entry
3. Mark the project folder as published

---

## Error Handling

If an error occurs at any step:

- Log the error with full context (step, command, error message)
- Do not skip to the next step
- Report blocking errors with a suggested fix
- Never force-publish content with known issues

---

## Publishing Checklist

- [ ] checklist.md confirms all review checks pass
- [ ] Critical edits from edits.md are applied
- [ ] Frontmatter is complete with title, pubDate, and all required fields
- [ ] Post file created at SITE/src/content/blog/<slug>.md
- [ ] All artifacts copied to public directory
- [ ] Post renders correctly in local preview
- [ ] Production build succeeds
- [ ] Status updated to published in ideas.yaml
