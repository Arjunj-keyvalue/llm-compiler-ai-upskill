from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import asyncio

from .config import settings
from .logger import get_logger
from app.agents import get_response


class AgentRequest(BaseModel):
    prompt: str

app = FastAPI()
logger = get_logger(__name__)

# Mount the 'static' directory
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
async def read_root():
    return FileResponse(os.path.join(static_dir, 'index.html'))

@app.post("/agent")
def run_agent(request: AgentRequest):
    # Placeholder for agentic AI logic
    # In a real application, this is where you would interact with your local LLM
    logger.info(f"Received prompt: {request.prompt}")
    return {"response": f"Processing your request: '{request.prompt}'"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    config = {"recursion_limit": 50}
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f"Received data: {data}")
            await websocket.send_text(get_response(data))
            await websocket.send_text("[END]")
    except WebSocketDisconnect:
        logger.info("Client disconnected")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.app_host, port=settings.app_port)