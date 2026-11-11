class FakeDatabase:
    """
    模拟数据库。
    """

    def __init__(self, records):
        self.records = records

    def fetch_page(self, offset, page_size):
        """
        模拟分页查询。
        """

        return self.records[
            offset:offset + page_size
        ]


class DatabaseIterator:
    """
    数据库分页迭代器。

    每次 next() 最多读取一页，
    并逐条返回当前页中的记录。
    """

    def __init__(self, database, page_size=2):
        if page_size <= 0:
            raise ValueError("page_size 必须大于 0")

        self.database = database
        self.page_size = page_size

        self.offset = 0
        self.buffer = []
        self.buffer_index = 0
        self.finished = False

    def __iter__(self):
        return self

    def __next__(self):

        # 当前页已经读取完毕，需要获取下一页
        if self.buffer_index >= len(self.buffer):

            if self.finished:
                raise StopIteration

            self.buffer = self.database.fetch_page(
                self.offset,
                self.page_size
            )

            self.offset += len(self.buffer)
            self.buffer_index = 0

            if not self.buffer:
                self.finished = True
                raise StopIteration

        record = self.buffer[self.buffer_index]

        self.buffer_index += 1

        return record


def main():

    records = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
        {"id": 4, "name": "David"},
        {"id": 5, "name": "Eve"},
    ]

    database = FakeDatabase(records)

    iterator = DatabaseIterator(
        database,
        page_size=2
    )

    for record in iterator:
        print(record)


if __name__ == "__main__":
    main()