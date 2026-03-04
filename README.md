# CUBE 7 Claude Code Skill

A [Claude Code](https://claude.ai/claude-code) skill that answers questions about **Bentley CUBE 7** (CUBE CONNECT Edition) travel demand modeling software, backed by the full scraped official documentation.

## What it is

- A custom Claude Code skill (`SKILL.md`) that instructs Claude to search and read local CUBE 7 docs before answering
- 386 Markdown files scraped from the Bentley CUBE 7 official documentation, covering Voyager scripting, Highway, PT, Matrix, CubePy, and more
- A scraper (`scraper.py`) to regenerate the docs from the Bentley website

## Prerequisites

- [Claude Code CLI](https://claude.ai/claude-code) installed
- Git

## Quick Start

```bash
git clone https://github.com/taotao/cube-claude-skill.git
cd cube-claude-skill
claude
```

Then ask any CUBE question, for example:

> How do I use the MATRIX application in Cube Voyager?

> What is the syntax for IF/ELSEIF in a Voyager script?

> How do I set up distributed computing with CUBE Cluster?

Claude will automatically use the skill to search the local documentation and give you an accurate, doc-grounded answer.

## How the Skill Works

When you ask a CUBE-related question, Claude Code activates the `cube` skill which:

1. **Searches** the `output/` directory using keyword grep across all 386 documentation files
2. **Reads** the most relevant files in full
3. **Synthesizes** a direct answer with citations to the source documentation pages

The skill covers:
- Getting Started and migration to CUBE 7
- CUBE Base: Project Explorer, Application Manager, Scenario Manager, Catalog Manager
- CUBE Voyager: Highway, PT, Matrix, Walk, PILOT, FREQ applications
- Voyager scripting syntax: variables, keywords, control flow, file I/O
- GIS Window, Network Editor, Map Publisher
- CubePy Python library
- CUBE Cluster (distributed computing)
- File formats and viewers

## Regenerating the Documentation

The `output/` docs are included in this repo, but you can re-scrape them from the Bentley website:

```bash
pip install -r requirements.txt
python scraper.py
```

This will overwrite the files in `output/` with fresh content from the Bentley CUBE 7 documentation site.

## Documentation Copyright

The scraped documentation files in `output/` are copyright Bentley Systems. They are included here solely to enable the Claude Code skill to function offline. Refer to [Bentley's terms of use](https://www.bentley.com/legal/) for usage restrictions.

## License

The skill code (SKILL.md), scraper, and other non-documentation files are MIT licensed. See [LICENSE](LICENSE).
