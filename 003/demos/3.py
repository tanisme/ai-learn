def data_processor():

    print("生成器启动")

    while True:

        value = yield

        print("收到数据:", value)


generator = data_processor()

# 启动生成器
next(generator)

generator.send(100)
generator.send(200)
generator.send(300)

print("*" * 100)
def accumulator():

    total = 0

    while True:

        value = yield total

        if value is None:
            continue

        total += value


generator = accumulator()

# 启动生成器
print(next(generator))

print(generator.send(10))
print(generator.send(20))
print(generator.send(30))
print("*" * 100)
def generator():

    try:
        yield 1
        yield 2

    except ValueError:
        print("生成器内部捕获到 ValueError")

    yield 3


g = generator()

print(next(g))
print(g.throw(ValueError("测试异常")))
print("*" * 100)

def generator():

    try:

        while True:
            yield 1

    finally:
        print("生成器正在清理资源")


g = generator()

print(next(g))

g.close()
print("*" * 100)
def read_file(path):

    file = open(path, "r", encoding="utf-8")

    try:

        for line in file:
            yield line.rstrip("\n")

    finally:

        file.close()
        print("文件资源已释放")


generator = read_file("data.txt")

try:
    print(next(generator))
finally:
    generator.close()
print("*" * 100)
import sys


numbers_list = [x for x in range(1000000)]

numbers_generator = (
    x for x in range(1000000)
)

print(
    "列表大小:",
    sys.getsizeof(numbers_list)
)

print(
    "生成器对象大小:",
    sys.getsizeof(numbers_generator)
)
print("*" * 100)
def retrieve_documents():

    for i in range(100000):

        yield {
            "id": i,
            "content": f"document content {i}"
        }


def filter_documents(documents):

    for document in documents:

        if document["id"] % 2 == 0:
            yield document


def build_context(documents):

    for document in documents:

        yield {
            "id": document["id"],
            "context": document["content"]
        }


documents = retrieve_documents()

filtered = filter_documents(documents)

contexts = build_context(filtered)

for context in contexts:
    print(context)

    if context["id"] >= 4:
        break
print("*" * 100)
print("*" * 100)