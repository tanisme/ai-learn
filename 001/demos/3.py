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