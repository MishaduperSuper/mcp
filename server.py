from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Cool MCP on Render 😎")

@mcp.tool()
def chat_reply(text: str) -> str:
    return f"🤖 MCP (Render) получил: {text}"

@mcp.tool()
def calc(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run(transport="sse")
