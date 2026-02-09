.DEFAULT_GOAL := help
SHELL := /bin/bash
export VALIDATE_PY

.PHONY: help setup preview build deploy test validate

define VALIDATE_PY
import yaml, sys, glob
files = glob.glob('BACKLOG/*.yaml') + glob.glob('TOOLS/*.yaml')
errors = 0
for f in files:
    try:
        yaml.safe_load(open(f))
        print(f'  OK  {f}')
    except yaml.YAMLError as e:
        print(f'  FAIL {f}: {e}')
        errors += 1
if errors:
    sys.exit(1)
endef

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Install skills, site dependencies, and Playwright
	@echo "==> Setting up Grimshaw Studio..."
	@if [ -x scripts/setup-skills.sh ]; then \
		echo "--- Running setup-skills.sh"; \
		scripts/setup-skills.sh; \
	else \
		echo "--- scripts/setup-skills.sh not found or not executable, skipping"; \
	fi
	@echo "--- Installing SITE/ npm dependencies"
	cd SITE && npm install
	@echo "--- Installing Playwright browsers"
	cd SITE && npx playwright install
	@echo "==> Setup complete."

preview: ## Start Astro dev server for local preview
	cd SITE && npm run dev

build: ## Build the Astro site (output in SITE/dist/)
	cd SITE && npm run build

deploy: ## Deploy by pushing main branch to origin
	git push origin main

test: ## Discover and test all artifacts
	@echo "==> Running artifact tests..."
	@pass=0; fail=0; skip=0; \
	if [ -x scripts/test-artifact.sh ]; then \
		for f in $$(find PROJECTS BRAND SITE -name '*.html' -path '*/artifacts/*' 2>/dev/null); do \
			echo "--- Testing $$f"; \
			if scripts/test-artifact.sh "$$f"; then \
				pass=$$((pass + 1)); \
			else \
				fail=$$((fail + 1)); \
			fi; \
		done; \
		if [ -f scripts/fixtures/good-artifact.html ]; then \
			echo "--- Testing fixture: good-artifact.html"; \
			if scripts/test-artifact.sh scripts/fixtures/good-artifact.html; then \
				pass=$$((pass + 1)); \
			else \
				fail=$$((fail + 1)); \
			fi; \
		fi; \
		if [ -f scripts/fixtures/bad-artifact.html ]; then \
			echo "--- Testing fixture: bad-artifact.html (expect failure)"; \
			if scripts/test-artifact.sh scripts/fixtures/bad-artifact.html; then \
				fail=$$((fail + 1)); \
				echo "    UNEXPECTED PASS (should have failed)"; \
			else \
				pass=$$((pass + 1)); \
				echo "    Expected failure, OK"; \
			fi; \
		fi; \
	else \
		echo "--- scripts/test-artifact.sh not found, skipping artifact tests"; \
		skip=1; \
	fi; \
	echo "==> Results: $$pass passed, $$fail failed, $$skip skipped"; \
	if [ $$fail -gt 0 ]; then exit 1; fi

validate: ## Validate YAML files using Python
	@echo "==> Validating YAML files..."
	@python3 -c "$$VALIDATE_PY"
	@echo "==> Validation complete."
