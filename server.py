import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("NextJs_Workspace")

# This is the exact name of your folder and future GitHub repo
PROJECT_NAME = "."
PROJECT_DIR = f"./{PROJECT_NAME}"

# 1. The server automatically creates the folder when it starts
os.makedirs(PROJECT_DIR, exist_ok=True)

@mcp.tool()
def write_code_file(file_path: str, content: str) -> str:
    """Writes or updates a file inside the Next.js project."""
    safe_path = os.path.normpath(os.path.join(PROJECT_DIR, file_path))
    
    # Security check to keep AI inside the folder
    if not safe_path.startswith(os.path.abspath(PROJECT_DIR)):
        return "Error: Path is outside the project directory."

    os.makedirs(os.path.dirname(safe_path), exist_ok=True)
    with open(safe_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Successfully wrote to {file_path}"

@mcp.tool()
def read_code_file(file_path: str) -> str:
    """Reads a file from the Next.js project."""
    safe_path = os.path.normpath(os.path.join(PROJECT_DIR, file_path))
    if os.path.exists(safe_path):
        with open(safe_path, "r", encoding="utf-8") as f:
            return f.read()
    return f"File {file_path} not found."