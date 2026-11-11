import asyncio


async def generate_data():

    for i in range(20):
        yield i


async def process(item, semaphore):

    async with semaphore:

        await asyncio.sleep(1)

        print("处理完成:", item)


async def main():

    semaphore = asyncio.Semaphore(5)

    tasks = []

    async for item in generate_data():

        task = asyncio.create_task(
            process(item, semaphore)
        )

        tasks.append(task)

    await asyncio.gather(*tasks)


asyncio.run(main())