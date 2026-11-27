"""PostToolUse hook: run `ruff check --fix` after Claude runs a `git commit` via Bash.

Claude Code passes the tool call as JSON on stdin. Hook matchers only see the
tool name, so the command filter has to happen here.
"""

import json
import os
import re
import subprocess
import sys

GIT_COMMIT = re.compile(r"\bgit\s+commit\b")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    command = payload.get("tool_input", {}).get("command", "")
    if not GIT_COMMIT.search(command):
        return 0

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    subprocess.run(
        ["uvx", "ruff@0.17.6", "check", ".", "--fix", "--silent"],
        cwd=project_dir,
        check=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
