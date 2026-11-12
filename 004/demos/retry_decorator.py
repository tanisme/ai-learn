import time

from functools import wraps


def retry(
    max_attempts=3,
    delay=1,
    exceptions=(Exception,)
):
    """
    重试装饰器。

    参数：
        max_attempts:
            最大尝试次数。

        delay:
            每次失败后的等待时间。

        exceptions:
            需要捕获并重试的异常类型。
    """

    if max_attempts <= 0:
        raise ValueError("max_attempts 必须大于 0")

    if delay < 0:
        raise ValueError("delay 不能小于 0")

    if not isinstance(exceptions, tuple):
        raise TypeError("exceptions 必须是异常类型元组")

    if not exceptions or not all(
        isinstance(exc, type) and issubclass(exc, BaseException)
        for exc in exceptions
    ):
        raise TypeError("exceptions 必须包含异常类型")

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(1, max_attempts + 1):

                try:

                    print(
                        f"[Retry] 第 {attempt} 次执行: "
                        f"{func.__name__}"
                    )

                    return func(*args, **kwargs)

                except exceptions as exc:

                    last_exception = exc

                    print(
                        f"[Retry] 执行失败: {exc}"
                    )

                    if attempt == max_attempts:
                        break

                    time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator


# 模拟模型调用
class MockLLM:

    def __init__(self):
        self.count = 0

    def invoke(self, prompt):

        self.count += 1

        if self.count < 3:
            raise ConnectionError("模型服务暂时不可用")

        return f"模型回答: {prompt}"


llm = MockLLM()


@retry(
    max_attempts=3,
    delay=1,
    exceptions=(ConnectionError,)
)
def call_llm(prompt):

    return llm.invoke(prompt)


if __name__ == "__main__":

    result = call_llm("解释 Python 装饰器")

    print(result)