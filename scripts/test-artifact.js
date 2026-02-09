#!/usr/bin/env node
/**
 * test-artifact.js - Loads an HTML file in headless Chromium via Playwright
 * and checks for console errors.
 *
 * Usage: node scripts/test-artifact.js <path-to-html-file>
 *
 * Exit codes:
 *   0 - No console errors found
 *   1 - Console errors detected (details on stderr)
 *   2 - Usage / file error
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function main() {
  const htmlPath = process.argv[2];

  if (!htmlPath) {
    process.stderr.write('Usage: node test-artifact.js <path-to-html-file>\n');
    process.exit(2);
  }

  const resolved = path.resolve(htmlPath);

  if (!fs.existsSync(resolved)) {
    process.stderr.write(`File not found: ${resolved}\n`);
    process.exit(2);
  }

  const fileUrl = `file://${resolved}`;
  const errors = [];

  let browser;
  try {
    browser = await chromium.launch({ headless: true });
    const context = await browser.newContext();
    const page = await context.newPage();

    // Capture console.error messages
    page.on('console', (msg) => {
      if (msg.type() === 'error') {
        errors.push(msg.text());
      }
    });

    // Capture page-level errors (uncaught exceptions)
    page.on('pageerror', (err) => {
      errors.push(err.message);
    });

    await page.goto(fileUrl, { waitUntil: 'load', timeout: 15000 });

    // Give a brief moment for any deferred errors to fire
    await page.waitForTimeout(500);

    await browser.close();
    browser = null;

    if (errors.length > 0) {
      process.stderr.write(`Console errors found in ${htmlPath}:\n`);
      for (const err of errors) {
        process.stderr.write(`  - ${err}\n`);
      }
      process.exit(1);
    }

    process.stdout.write(`No console errors in ${htmlPath}\n`);
    process.exit(0);
  } catch (err) {
    process.stderr.write(`Failed to test artifact: ${err.message}\n`);
    if (browser) await browser.close();
    process.exit(1);
  }
}

main();
