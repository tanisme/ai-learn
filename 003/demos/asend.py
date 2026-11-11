import asyncio


async def data_processor():

    print("处理器启动")

    while True:

        value = yield

        print("收到数据:", value)


async def main():

    generator = data_processor()

    # 启动异步生成器
    await generator.asend(None)

    await generator.asend(100)
    await generator.asend(200)
    await generator.asend(300)

    await generator.aclose()


if __name__ == "__main__":
    asyncio.run(main())