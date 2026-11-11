import asyncio
from typing import AsyncIterator

from app.events import AgentEvent
from app.generators import generate_tokens


class StreamingAgent:
    """
    简化的流式 Agent。

    执行过程：

    1. 开始执行
    2. 进入分析节点
    3. 模拟模型流式输出
    4. 完成执行
    """

    def __init__(self, token_delay: float = 0.1):
        self.token_delay = token_delay

    async def run(
        self,
        prompt: str
    ) -> AsyncIterator[AgentEvent]:
        """
        执行 Agent 并持续产生事件。
        """

        if not prompt.strip():
            yield AgentEvent(
                event="error",
                data={
                    "message": "Prompt 不能为空"
                }
            )
            return

        try:

            # 1. Agent 开始
            yield AgentEvent(
                event="run_start",
                data={
                    "prompt": prompt
                }
            )

            # 2. 分析节点开始
            yield AgentEvent(
                event="node_start",
                data={
                    "node": "analysis"
                }
            )

            await asyncio.sleep(0.2)

            # 3. 节点结束
            yield AgentEvent(
                event="node_end",
                data={
                    "node": "analysis"
                }
            )

            # 4. 模拟 LLM 生成
            yield AgentEvent(
                event="node_start",
                data={
                    "node": "llm"
                }
            )

            response = (
                "Python 生成器可以实现 "
                "高效的流式数据处理。"
            )

            async for token in generate_tokens(
                response,
                delay=self.token_delay
            ):

                yield AgentEvent(
                    event="token",
                    data={
                        "content": token
                    }
                )

            # 5. LLM 节点结束
            yield AgentEvent(
                event="node_end",
                data={
                    "node": "llm"
                }
            )

            # 6. Agent 结束
            yield AgentEvent(
                event="done",
                data={
                    "status": "completed"
                }
            )

        except asyncio.CancelledError:
            # 取消信号不能被吞掉
            raise

        except Exception as exc:

            yield AgentEvent(
                event="error",
                data={
                    "message": str(exc)
                }
            )