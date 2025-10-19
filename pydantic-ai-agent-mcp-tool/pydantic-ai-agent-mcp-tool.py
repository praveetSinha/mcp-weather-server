import asyncio
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

# load the env variables from the .env file
load_dotenv()

# like a CLI command line running thing
server = MCPServerStdio(
    command= "C:\\Users\\prave\\.local\\bin\\uv.exe",
      args = [
        "--directory",
        "C:\\Users\\prave\\OneDrive\\Desktop\\FILES\\udemy\\project 4\\build-mcp-server",
        "run",
        "weather.py"
    ],
)

agent = Agent(
    model = "groq:llama-3.3-70b-versatile",
    toolsets=[server]
)

async def main():
    async with agent:
        result = await agent.run("What is the current weather in new delhi?")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
