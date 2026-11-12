import time

from functools import wraps


def measure_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        try:

            return func(*args, **kwargs)

        finally:

            elapsed = (
                time.perf_counter() - start
            )

            print(
                f"[Timing] {func.__name__}: "
                f"{elapsed:.4f}s"
            )

    return wrapper


@measure_time
def execute_agent():

    time.sleep(1)

    return "Agent 完成"


if __name__ == "__main__":

    result = execute_agent()

    print(result)