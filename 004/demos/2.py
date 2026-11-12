from functools import wraps


def handle_exception(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:

            return func(*args, **kwargs)

        except ValueError as exc:

            print(
                f"[Business Error] {exc}"
            )

            raise

        except Exception as exc:

            print(
                f"[System Error] {exc}"
            )

            raise

    return wrapper


@handle_exception
def execute_agent(prompt):

    if not prompt:
        raise ValueError("Prompt 不能为空")

    return "执行成功"


execute_agent("Hello")