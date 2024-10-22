from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.chat import chat, execute

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ExecuteRequest(BaseModel):
    code: str
    mode: str = None

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        result = await chat(request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/execute")
async def execute_endpoint(request: ExecuteRequest):
    try:
        result = await execute(request.code, request.mode)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
