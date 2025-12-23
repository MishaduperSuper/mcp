import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Cool MCP on Render 😎")

@mcp.tool()
def chat_reply(text: str) -> str:
    """Отвечает на сообщение"""
    return f"🤖 MCP (Render) получил: {text}"

@mcp.tool()
def calc(a: int, b: int) -> int:
    """Складывает числа"""
    return a + b

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="sse", port=port)
