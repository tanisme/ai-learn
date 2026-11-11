import asyncio
import json

from fastapi import FastAPI
from fastapi.responses import StreamingResponse


app = FastAPI()


async def generate_tokens():
    """
    模拟 LLM Token 流式生成。
    """

    tokens = [
        "Python ",
        "生成器 ",
        "可以 ",
        "实现 ",
        "流式 ",
        "数据 ",
        "处理。"
    ]

    for token in tokens:

        # 模拟模型生成延迟
        await asyncio.sleep(0.5)

        yield token


async def sse_event_generator():
    """
    将 Token 转换为 SSE 事件。
    """

    try:

        async for token in generate_tokens():

            event_data = {
                "content": token
            }

            yield (
                "event: token\n"
                f"data: {json.dumps(event_data, ensure_ascii=False)}\n\n"
            )

        # 发送结束事件
        yield (
            "event: done\n"
            "data: {}\n\n"
        )

    except asyncio.CancelledError:
        # 客户端断开等情况可能导致任务取消
        print("SSE 客户端连接已取消")
        raise

    except Exception as exc:

        error_data = {
            "message": str(exc)
        }

        yield (
            "event: error\n"
            f"data: {json.dumps(error_data, ensure_ascii=False)}\n\n"
        )


@app.get("/stream")
async def stream():

    return StreamingResponse(
        sse_event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


@app.get("/")
async def index():

    return {
        "message": "SSE Demo",
        "stream": "/stream"
    }