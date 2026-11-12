def outer():
    def inner():
        print("执行内部函数 inner")
    return inner

print(outer.__name__)
print(outer.__doc__)
print(outer.__module__)
print(outer.__defaults__)

func = outer()

func()

def execute_with_logging(func):

    print("开始执行:", func.__name__)

    result = func()

    print("执行结束:", func.__name__)

    return result


def run_agent():
    print("Agent 正在执行")

    return "Agent Result"


result = execute_with_logging(run_agent)

print(result)

print("----------------" * 3)
def outer():

    message = "Hello Closure"

    def inner():
        print(message)

    return inner


func = outer()
func()
print(func.__closure__)
print(func.__closure__[0].cell_contents)
print(func.__code__.co_freevars)
print("----------------" * 3)
def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = create_counter()
print(counter())
print(counter())
print(counter())
print("----------------" * 3)

def level_one():
    a = "A"

    def level_two():
        b = "B"

        def level_three():
            print(a, b)
        return level_three
    return level_two

func = level_one()()
func()
print(func.__code__.co_freevars)

for cell in func.__closure__:
    print(cell.cell_contents)
print("----------------" * 3)

def create_agent(model_name, temperature):
    def run(prompt):
        print("模型：", model_name)
        print("温度：", temperature)
        print("提示词：", prompt)
    return run

agent_a = create_agent("deepseek-flash", 0.3)
agent_b = create_agent("deepseek-pro", 0.2)
agent_a("分析 Python 生成器")
agent_b("编写一个故事")
print("----------------" * 3)

def log_execution(func):

    def wrapper():

        print("执行开始")

        result = func()

        print("执行结束")

        return result

    return wrapper

def run_agent():

    print("Agent 执行中")

    return "执行结果"


run_agent = log_execution(run_agent)

result = run_agent()

print(result)

print("----------------" * 3)

@log_execution
def run_agent1():
    print("Agent1 执行中")
    return "执行结果"

print(run_agent1())


print("----------------" * 3)

def decorator(func):
    print("装饰器执行")

    def wrapper():
        print("wrapper执行")
        return func()
    return wrapper

@decorator
def test():
    print("test执行")

print("程序开始")

test()




print("----------------" * 3)
# 实现通用参数传递。
from functools import wraps
def log_execution1(func):
    @wraps(func) #复制原始函数的重要元数据，并设置 __wrapped__，方便调试、文档生成和部分反射工具获取原始函数信息。
    def wrapper(*args, **kwargs):
        print("执行开始")
        result = func(*args, **kwargs)
        print("执行结束")
        return result
    return wrapper

@log_execution1
def add(a, b):
    return a + b

@log_execution1
def greet(name, age=None):
    return {
        "name": name,
        "age": age
    }

print(add(1, 2))
print(greet("Alice", 30))


print("----------------" * 3)
print("----------------" * 3)
print("----------------" * 3)
print("----------------" * 3)