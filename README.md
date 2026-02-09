# Grimshaw Studio

Content creation studio -- brand guidelines, prompt chains, and tooling for producing consistent, high-quality content.

## Structure

```
BRAND/          Brand voice, style, and visual guidelines
BACKLOG/        Ideas pipeline and series metadata
PROJECTS/       Active content projects
PROMPTS/        Prompt chain templates (ideate -> draft -> review -> publish)
TOOLS/          Automation and helper scripts
scripts/        Build and utility scripts
```

## Getting Started

```bash
make help    # Show all available commands
make setup   # Install dependencies and skills
make preview # Start local dev server
make build   # Build the Astro site
make test    # Run artifact tests
make validate # Validate YAML files
make deploy  # Push main branch to origin
```

## Deployment

The site auto-deploys to [macegrim.github.io](https://macegrim.github.io) on every push to `main` via GitHub Actions.

### DEPLOY_TOKEN Setup

The workflow requires a `DEPLOY_TOKEN` secret to push the built site to the `macegrim/macegrim.github.io` repository.

1. Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens?type=beta) (fine-grained tokens recommended)
2. Click **Generate new token**
3. Give it a descriptive name (e.g., `grimshaw-studio-deploy`)
4. Under **Repository access**, select **Only select repositories** and choose `macegrim/macegrim.github.io`
5. Under **Permissions > Repository permissions**, grant **Contents: Read and write**
6. Click **Generate token** and copy the token value
7. Go to the `grimshaw-studio` repo **Settings > Secrets and variables > Actions**
8. Click **New repository secret**
9. Name: `DEPLOY_TOKEN`, Value: paste the token from step 6
10. Click **Add secret**

The workflow will now automatically build the Astro site and push it to `macegrim.github.io` on every push to `main`.
