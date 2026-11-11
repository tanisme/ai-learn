import sys


def show_ref_count(name, obj):
    print(
        f"{name}: "
        f"ref_count={sys.getrefcount(obj)}"
    )


data = [10, 20, 30]

show_ref_count("初始状态", data)

other = data

show_ref_count("新增引用", data)

del other

show_ref_count("删除引用", data)

del data

print("data 已经删除")


import gc
import weakref

# 查看垃圾回收器是否启用
print(gc.isenabled())

# 查看当前垃圾回收统计
print(gc.get_stats())

# 手动执行垃圾回收
collected = gc.collect()

print("回收对象数量:", collected)

# 查看垃圾回收阈值
print(gc.get_threshold())

# 查看当前各代对象数量
print(gc.get_count())

print("=" * 100)
class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None


# 确保自动垃圾回收已开启
gc.enable()

a = Node("A")
b = Node("B")

a.ref = b
b.ref = a

# 创建弱引用，不增加目标对象的强引用计数
weak_a = weakref.ref(a)
weak_b = weakref.ref(b)

print("创建对象:", weak_a() is not None)
print("创建对象:", weak_b() is not None)

# 删除外部引用
del a
del b

# 此时循环可能仍然存在
print("回收前 A:", weak_a() is not None)

# 手动触发垃圾回收
gc.collect()

print("回收后 A:", weak_a())
print("回收后 B:", weak_b())


print("=" * 100)
import sys

number = 100
name = "Agent"
items = [1, 2, 3]

print(sys.getsizeof(number))
print(sys.getsizeof(name))
print(sys.getsizeof(items))

data = [[1, 2, 3], [4, 5, 6]]

print(sys.getsizeof(data))
print(sys.getsizeof(data[0]))

print("=" * 100)
a = [1, 2, 3]

b = a

c = a.copy()

b.append(4)

c.append(5)

print(a)
print(b)
print(c)

print(a is b)
print(a is c)

print(a == c)


import tracemalloc


class DataManager:

    def __init__(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)


def main():

    # 开启内存追踪
    tracemalloc.start()

    manager = DataManager()

    # 保存初始快照
    snapshot1 = tracemalloc.take_snapshot()

    # 模拟不断累积数据
    for i in range(100000):
        manager.add_data({
            "id": i,
            "name": f"user-{i}",
            "content": "Agent memory test" * 10
        })

    # 保存第二次快照
    snapshot2 = tracemalloc.take_snapshot()

    # 对比两次快照
    statistics = snapshot2.compare_to(
        snapshot1,
        "lineno"
    )

    print("内存分配增长情况:")

    for stat in statistics[:10]:
        print(stat)

    current, peak = tracemalloc.get_traced_memory()

    print("当前追踪内存:", current / 1024 / 1024, "MB")
    print("峰值追踪内存:", peak / 1024 / 1024, "MB")

    tracemalloc.stop()

def weakref():
    import weakref

    class Agent:
        def __init__(self, name):
            self.name = name

    agent = Agent("ResearchAgent")

    # 创建弱引用
    agent_ref = weakref.ref(agent)

    print(agent_ref().name)

    # 删除强引用
    del agent

    # 目标对象被销毁后，弱引用返回 None
    print(agent_ref())

if __name__ == "__main__":
    main()
    weakref()