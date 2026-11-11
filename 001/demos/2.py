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