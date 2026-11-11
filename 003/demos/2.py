def get_numbers():
    print("开始执行")

    yield 1

    print("继续执行")

    yield 2

    print("执行结束")


generator = get_numbers()

print("生成器已经创建")

print(next(generator))
print(next(generator))


def counter():
    count = 0

    while count < 3:
        count += 1

        yield count


generator = counter()

print(next(generator))
print(next(generator))
print(next(generator))


def number_range(start, stop, step=1):

    if step == 0:
        raise ValueError("step 不能为 0")

    current = start

    if step > 0:
        while current < stop:
            yield current
            current += step

    else:
        while current > stop:
            yield current
            current += step


print(list(number_range(1, 6)))
print(list(number_range(5, 0, -1)))

print("*" * 100)
def child_generator():
    yield 1
    yield 2
    yield 3


def parent_generator():

    for value in child_generator():
        yield value


for value in parent_generator():
    print(value)

def parent_generator():
    yield from child_generator()


for value in parent_generator():
    print(value)

print("*" * 100)
def source_a():
    yield "A1"
    yield "A2"


def source_b():
    yield "B1"
    yield "B2"


def combined_generator():

    yield from source_a()

    yield from source_b()


for item in combined_generator():
    print(item)


print("*" * 100)
def retrieval_events():
    yield {"type": "retrieval", "content": "开始检索"}
    yield {"type": "retrieval", "content": "检索完成"}


def tool_events():
    yield {"type": "tool", "content": "调用搜索工具"}
    yield {"type": "tool", "content": "工具执行完成"}


def llm_events():
    yield {"type": "token", "content": "这是"}
    yield {"type": "token", "content": "最终回答"}


def agent_pipeline():

    yield from retrieval_events()

    yield from tool_events()

    yield from llm_events()


for event in agent_pipeline():
    print(event)