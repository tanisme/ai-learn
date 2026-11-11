import asyncio
from typing import AsyncIterator


async def generate_tokens(
    text: str,
    delay: float = 0.1
) -> AsyncIterator[str]:
    """
    模拟 LLM Token 流式生成。

    这里按照空格切分文本，模拟 Token。
    真实项目中应该使用 LLM 的 astream()。
    """

    if delay < 0:
        raise ValueError("delay 不能小于 0")

    tokens = text.split(" ")

    for index, token in enumerate(tokens):

        await asyncio.sleep(delay)

        # 保留原始空格
        if index < len(tokens) - 1:
            token += " "

        yield token