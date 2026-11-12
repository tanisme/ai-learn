from functools import wraps


TOOL_REGISTRY = {}


def tool(name=None):

    def decorator(func):

        tool_name = name or func.__name__

        if tool_name in TOOL_REGISTRY:

            raise ValueError(
                f"工具重复注册: {tool_name}"
            )

        TOOL_REGISTRY[tool_name] = func

        @wraps(func)
        def wrapper(*args, **kwargs):

            return func(*args, **kwargs)

        return wrapper

    return decorator


@tool(name="search")
def search_web(query):

    return f"搜索结果: {query}"


@tool(name="calculator")
def calculate(expression):

    return f"计算表达式: {expression}"


def execute_tool(name, **kwargs):

    func = TOOL_REGISTRY.get(name)

    if func is None:

        raise ValueError(
            f"工具不存在: {name}"
        )

    return func(**kwargs)


if __name__ == "__main__":

    print(TOOL_REGISTRY.keys())

    print(
        execute_tool(
            "search",
            query="Python Decorator"
        )
    )