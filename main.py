import random, json
from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="Simple calculator server")

@mcp.tool
def Add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool
def roll_dice(min_value: int = 1, max_value: int = 100) -> int:

    """Roll a dice between min_value and max_value and return the results."""

    return random.randint(min_value, max_value)

@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server."""
    info = {
        "name": "Simple calculator server",
        "version": "1.0.0",
        "description": "A MCP with maths tools.",
        "tools": ["Add_numbers", "roll_dice"],
        "author": "Pramod Carpenter"

    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)