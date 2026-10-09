from fastapi import FastAPI, Request
import hashlib

app = FastAPI()

EMAIL = "24f2004978@ds.study.iitm.ac.in"


@app.post("/")
async def mcp(request: Request):
    body = await request.json()
    
    method = body.get("method")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "protocolVersion": "2025-06-18",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "exam-mcp-server",
                    "version": "1.0.0"
                }
            }
        }

    if method == "notifications/initialized":
        return {}

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "tools": [
                    {
                        "name": "solve_challenge",
                        "description": "Solve the exam challenge",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    }
                ]
            }
        }

    if method == "tools/call":
        challenge = request.headers.get("X-Exam-Challenge", "")

        normalized_email = EMAIL.strip().lower()

        value = f"{challenge}:{normalized_email}"

        answer = hashlib.sha256(value.encode()).hexdigest()[:16]

        return {
            "jsonrpc": "2.0",
            "id": body.get("id"),
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": answer
                    }
                ]
            }
        }

    return {
        "jsonrpc": "2.0",
        "id": body.get("id"),
        "error": {
            "code": -32601,
            "message": "Method not found"
        }
    }