from mcp.server.fastmcp import FastMCP
import os
from openai import OpenAI        # ☆ v1 以降はクライアントクラスを使う
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "o3")

client = OpenAI(api_key=OPENAI_API_KEY)   # ☆ クライアント生成

mcp = FastMCP(title="o3 bridge", description="Relay prompts to OpenAI o3")

@mcp.tool(
    name="ask_o3",
    description="Send a prompt to OpenAI o3 and return its answer"
)
def ask_o3(prompt: str, system: str | None = None) -> dict:
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    # ☆ 新 API: client.chat.completions.create(...)
    resp = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=False,   # ← stream=True なら for chunk in resp: yield ...
    )
    content = resp.choices[0].message.content
    return {"answer": content}

if __name__ == "__main__":
    mcp.run()
