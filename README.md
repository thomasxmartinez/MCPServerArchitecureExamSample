# MCP Server Architecture Exam Sample

Project-scoped MCP setup for Claude Code. The servers are defined in `mcp_starter/.mcp.json`:

| Server | What it does | Runs via |
|---|---|---|
| `filesystem` | Read/write files in `mcp_starter/` | `npx` (Node) |
| `github` | GitHub API access | `npx` (Node), needs `GITHUB_TOKEN` |
| `summarizer` | Summarizes the repo's README and file list (`summarizer_server.py`) | `uv` (Python, pins `mcp<2`) |

## Prerequisites

- [Node.js](https://nodejs.org/) (provides `npx`)
- [uv](https://docs.astral.sh/uv/) (`brew install uv` on macOS)
- [Claude Code](https://docs.claude.com/en/docs/claude-code) (`claude`)
- A GitHub personal access token

No `npm install`, virtual environment, or build step is needed; `npx` and `uv` fetch dependencies on first run.

## Setup

```bash
cd mcp_starter
cp .env.example .env          # then put your token in .env
set -a; source .env; set +a   # Claude Code does not read .env on its own
claude                        # approve the project's MCP servers when prompted
```

Check the servers from `mcp_starter/`:

```bash
claude mcp list
```

All three should show `Connected`. `.env` is gitignored; never commit your token.
