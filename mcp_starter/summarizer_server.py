# summarizer_server.py

from mcp.server.fastmcp import FastMCP
import os
import subprocess

mcp = FastMCP("summarizer")

@mcp.tool()
def summarize_repo(path: str = ".") -> str:
    """Summarize the repository's README and top-level file structure.
    
    Returns a concatenated digest. Does not search file contents;
    use the filesystem server for contrent reads
    """

    files = subprocess.check_output(["git", "ls-files"], text=True).splitlines()[:50]
    readme = ""
    readme_path = os.path.join(path, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            readme = f.read()[:2000]
    return "Files (first 50):\n" + "\n".join(files) + f"\n\nReadme excerpt:\n{readme}"

if __name__ == "__main__":
    mcp.run(transport="stdio")