class NumberIterator:
    """
    自定义数字迭代器。

    从 start 开始，每次增加 step，
    最多产生 limit 个数字。
    """

    def __init__(self, start, limit, step=1):
        self.current = start
        self.limit = limit
        self.step = step
        self.count = 0

    def __iter__(self):
        # 迭代器返回自身
        return self

    def __next__(self):
        # 判断是否结束
        if self.count >= self.limit:
            raise StopIteration

        value = self.current

        self.current += self.step
        self.count += 1

        return value


def main():
    iterator = NumberIterator(
        start=10,
        limit=5,
        step=2
    )

    for number in iterator:
        print(number)


if __name__ == "__main__":
    main()