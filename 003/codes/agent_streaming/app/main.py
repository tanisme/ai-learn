import asyncio

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from app.agent import StreamingAgent


app = FastAPI(
    title="Agent Streaming Runtime",
    version="1.0.0"
)

agent = StreamingAgent(
    token_delay=0.3
)


@app.get("/")
async def index():

    return {
        "message": "Agent Streaming Runtime",
        "stream_api": "/agent/stream"
    }


@app.get("/agent/stream")
async def stream_agent(prompt: str):

    async def event_stream():

        try:

            async for event in agent.run(prompt):

                yield event.to_sse()

        except asyncio.CancelledError:

            print("Agent 流式任务被取消")

            raise

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )