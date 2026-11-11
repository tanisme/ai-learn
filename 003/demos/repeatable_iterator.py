class NumberRangeIterator:
    """
    具体迭代器。

    每个迭代器实例都有独立的遍历状态。
    """

    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.current >= self.stop:
                raise StopIteration
        elif self.step < 0:
            if self.current <= self.stop:
                raise StopIteration
        else:
            raise ValueError("step 不能为 0")

        value = self.current
        self.current += self.step

        return value


class NumberRange:
    """
    可迭代对象。

    自身不保存迭代进度。
    每次 iter() 都创建一个新的迭代器。
    """

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError("step 不能为 0")

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return NumberRangeIterator(
            self.start,
            self.stop,
            self.step
        )


def main():
    numbers = NumberRange(1, 6)

    print("第一次遍历：")

    for number in numbers:
        print(number)

    print("第二次遍历：")

    for number in numbers:
        print(number)

    print("两个迭代器独立运行：")

    iterator1 = iter(numbers)
    iterator2 = iter(numbers)

    print(next(iterator1))
    print(next(iterator1))

    print(next(iterator2))


if __name__ == "__main__":
    main()