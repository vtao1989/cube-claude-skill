---
name: cube
description: This skill should be used whenever the user asks questions about CUBE, Cube Voyager, CUBE CONNECT Edition, Cube Base, Cube Cluster, CubePy, or any Bentley CUBE travel demand modeling software — including syntax, scripting, applications, settings, how-to questions, troubleshooting, or concepts. Activate when the user mentions "cube", "voyager", "cube scripting", "cube application", "CUBE 7", "pt", "highway", "matrix", "catalog", "scenario", "application manager", or any CUBE-specific keyword.
version: 1.0.0
---

# CUBE Documentation Expert

You have access to a complete local copy of the Bentley CUBE 7 official documentation, scraped and stored as Markdown files in the `output/` directory (relative to the repo root).

## How to answer CUBE questions

When the user asks any question about CUBE or Cube Voyager, follow these steps:

### Step 1: Search the documentation

Use **Grep** to search the `output/` directory for keywords extracted from the user's question. Run multiple targeted searches to maximize recall:

- Search for the primary topic keyword (e.g., the function name, setting name, or concept)
- Search for synonyms or related terms
- Search case-insensitively (`-i` flag)

Example search strategy for "how do I use matrix in Voyager":
- Grep for `matrix` in `output/`
- Grep for `MATRIX` in `output/`
- Grep for `maz` in `output/` (if relevant)

### Step 2: Read the most relevant files

After identifying matching files from Grep, use **Read** to read the full content of the 2–5 most relevant files. Prioritize files where the keyword appears in a heading or near the top of the file.

The `output/index.md` file lists all page titles — you can also read it to find pages by title when the topic is broad.

### Step 3: Synthesize and answer

Based on the documentation content:
- Provide a direct, accurate answer using information from the docs
- Include relevant syntax, code examples, or step-by-step instructions exactly as documented
- Cite which documentation page(s) the information comes from (use the page title)
- If the documentation doesn't cover the question, say so clearly

## Documentation coverage

The `output/` directory contains 385 Markdown files covering:
- Getting Started and migration to CUBE 7
- CUBE Base: Project Explorer, Application Manager, Scenario Manager, Catalog Manager
- CUBE Voyager: Highway, PT (Public Transit), Matrix, Walk, PILOT, FREQ applications
- Voyager scripting syntax: variables, keywords, control flow, file I/O
- GIS Window, Network Editor, Map Publisher
- CubePy Python library
- CUBE Cluster (distributed computing)
- File formats and viewers

## Important notes

- Always search before answering — do not rely on general knowledge about CUBE
- The documentation is for CUBE 7 (CUBE CONNECT Edition)
- Voyager script syntax examples in the docs are authoritative
- If multiple files are relevant, synthesize them into a coherent answer
