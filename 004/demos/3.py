from functools import wraps


def require_role(required_role):

    def decorator(func):

        @wraps(func)
        def wrapper(user, *args, **kwargs):

            if user.get("role") != required_role:

                raise PermissionError(
                    "没有权限执行该操作"
                )

            return func(
                user,
                *args,
                **kwargs
            )

        return wrapper

    return decorator


@require_role("admin")
def delete_knowledge_base(user, kb_id):

    print(
        f"用户 {user['name']} 删除知识库 {kb_id}"
    )


admin = {
    "name": "Alice",
    "role": "admin"
}

normal_user = {
    "name": "Bob",
    "role": "user"
}


delete_knowledge_base(admin, "kb_001")

# 会抛出 PermissionError
# delete_knowledge_base(normal_user, "kb_001")