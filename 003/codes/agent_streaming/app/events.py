from dataclasses import dataclass
from typing import Any, Dict
import json


@dataclass
class AgentEvent:
    """
    Agent 统一事件模型。

    所有执行节点、工具调用、模型 Token
    都通过统一的事件结构向外传递。
    """

    event: str

    data: Dict[str, Any]

    def to_sse(self) -> str:
        """
        转换为 SSE 格式。
        """

        payload = json.dumps(
            self.data,
            ensure_ascii=False
        )

        return (
            f"event: {self.event}\n"
            f"data: {payload}\n\n"
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        转换为普通字典。
        """

        return {
            "event": self.event,
            "data": self.data
        }