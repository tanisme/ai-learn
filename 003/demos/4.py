import asyncio


async def generate_data():

    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def process(item):

    await asyncio.sleep(1)

    print("处理完成:", item)


async def main():

    async for item in generate_data():

        await process(item)


asyncio.run(main())