#!/bin/bash
# test-artifact.sh - Test an HTML artifact for console errors
#
# Usage: scripts/test-artifact.sh <path-to-html-file>
#
# Loads the given HTML file in a headless Chromium browser using Playwright
# and checks for console errors.
#
# Exit codes:
#   0 - No console errors found
#   1 - Console errors detected (details on stderr)
#   2 - Usage / file error

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <path-to-html-file>" >&2
  exit 2
fi

HTML_FILE="$1"

if [ ! -f "$HTML_FILE" ]; then
  echo "Error: File not found: $HTML_FILE" >&2
  exit 2
fi

# Ensure playwright is available
if ! node -e "require('playwright')" 2>/dev/null; then
  echo "Installing playwright..." >&2
  (cd "$PROJECT_ROOT" && npm install playwright 2>/dev/null)
  npx playwright install chromium 2>/dev/null
fi

# Run the Node.js test script
exec node "$SCRIPT_DIR/test-artifact.js" "$HTML_FILE"
