#!/usr/bin/env bash
#
# setup-skills.sh
#
# Creates symlinks from PROMPTS/skills/*.md to ~/.claude/commands/
# Idempotent: safe to run multiple times. Existing symlinks are updated,
# non-symlink files are never overwritten.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/PROMPTS/skills"
TARGET_DIR="$HOME/.claude/commands"

# Ensure target directory exists
mkdir -p "$TARGET_DIR"

# Ensure skills directory exists
if [ ! -d "$SKILLS_DIR" ]; then
    echo "ERROR: Skills directory not found: $SKILLS_DIR"
    exit 1
fi

linked=0
skipped=0

for skill_file in "$SKILLS_DIR"/*.md; do
    # Skip if no .md files match the glob
    [ -e "$skill_file" ] || continue

    filename="$(basename "$skill_file")"
    link_path="$TARGET_DIR/$filename"

    # If a symlink already exists, remove it and recreate (idempotent update)
    if [ -L "$link_path" ]; then
        rm "$link_path"
    elif [ -e "$link_path" ]; then
        echo "SKIP: $link_path exists and is not a symlink (not overwriting)"
        skipped=$((skipped + 1))
        continue
    fi

    ln -s "$skill_file" "$link_path"
    echo "LINKED: $filename -> $link_path"
    linked=$((linked + 1))
done

echo ""
echo "Done. $linked skill(s) linked, $skipped skipped."
