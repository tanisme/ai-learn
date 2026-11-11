import asyncio


class AsyncNumberIterator:
    """
    自定义异步迭代器。

    每次获取数据之前，模拟一次异步 I/O 操作。
    """

    def __init__(self, start, stop, delay=1):
        self.current = start
        self.stop = stop
        self.delay = delay

    def __aiter__(self):
        """
        返回异步迭代器自身。

        Python 3.7+ 中，__aiter__ 应直接返回异步迭代器，
        不应该定义为 async def。
        """
        return self

    async def __anext__(self):
        """
        异步获取下一个元素。
        """

        if self.current >= self.stop:
            raise StopAsyncIteration

        # 模拟异步 I/O
        await asyncio.sleep(self.delay)

        value = self.current

        self.current += 1

        return value


async def main():

    iterator = AsyncNumberIterator(
        start=1,
        stop=4,
        delay=0.5
    )

    async for number in iterator:
        print("获取数据:", number)


if __name__ == "__main__":
    asyncio.run(main())