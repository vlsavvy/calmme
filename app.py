from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CalmInput(BaseModel):
    heart_rate: int
    message: str = ""


CALMME_PROMPT = open("calmme_prompt.txt", encoding="utf-8").read()



def render_prompt(hr, msg):
    return CALMME_PROMPT.replace("{{heart_rate}}", str(hr)).replace("{{message}}", msg)


@app.post("/mcp/calmme")
def calm_logic(data: CalmInput):
    prompt = render_prompt(data.heart_rate, data.message)

    return {
        "type": "tool_call",
        "call": {
            "tool_name": "ambient_chat",
            "arguments": {
                "model": "ambient-1",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        }
    }


@app.get("/.well-known/agent.json")
def agent_card():
    return {
        "id": "calmme-mcp",
        "name": "CalmMe",
        "description": "A CBT-based emotional micro-intervention agent responding to real-time heart rate.",
        "type": "mcp",
        "version": "1.0.0",
        "endpoints": {
            "mcp": "https://calmme-kktmiavhe-vidhyalakshmi-bs-projects.vercel.app/mcp/calmme"
        }
    }


@app.get("/")
def root():
    return {"status": "CalmMe MCP Server Active"}

@app.get("/mcp/calmme")
def calmme_get():
    return {"message": "Send a POST request with heart_rate and message JSON to use this endpoint."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
