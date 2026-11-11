import asyncio

from langchain.chat_models import init_chat_model


llm = init_chat_model(
    model="deepseek:deepseek-flash",
    temperature=0
)


async def generate_llm_tokens(prompt):

    async for chunk in llm.astream(prompt):

        content = chunk.content

        if content:
            yield content


async def main():

    async for token in generate_llm_tokens(
        "请解释 Python 生成器的工作原理。"
    ):

        print(token, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())