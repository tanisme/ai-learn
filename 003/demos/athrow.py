import asyncio


async def generator():

    try:
        yield 1
        yield 2

    except ValueError:
        print("捕获 ValueError")

    yield 3


async def main():

    g = generator()

    print(await g.__anext__())

    print(
        await g.athrow(
            ValueError("测试异常")
        )
    )


asyncio.run(main())