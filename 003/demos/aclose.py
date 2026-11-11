import asyncio


async def generator():

    try:

        while True:
            yield "data"

    finally:
        print("执行异步生成器清理逻辑")


async def main():

    g = generator()

    print(await g.__anext__())

    await g.aclose()


asyncio.run(main())