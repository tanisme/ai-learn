import asyncio


async def generate_numbers():

    print("异步生成器启动")

    for i in range(1, 4):

        print("准备生成数据:", i)

        await asyncio.sleep(1)

        yield i

    print("异步生成器结束")


async def main():

    generator = generate_numbers()

    print("生成器已经创建")

    async for number in generator:
        print("消费数据:", number)


if __name__ == "__main__":
    asyncio.run(main())