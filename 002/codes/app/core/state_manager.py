from copy import copy, deepcopy
from typing import Any, Dict

from app.models.agent_state import AgentState


class StateManager:
    """
    Agent 状态管理器

    负责：
    1. 状态复制
    2. 状态更新
    3. 版本管理
    """

    @staticmethod
    def shallow_copy(
        state: AgentState
    ) -> AgentState:
        """
        浅拷贝状态
        """

        return state.model_copy()

    @staticmethod
    def deep_copy(
        state: AgentState
    ) -> AgentState:
        """
        深拷贝状态
        """

        return state.model_copy(deep=True)

    @staticmethod
    def update(
        state: AgentState,
        updates: Dict[str, Any]
    ) -> AgentState:
        """
        创建更新后的状态

        使用深拷贝隔离原状态，
        再对副本执行更新。
        """

        new_state = state.model_copy(deep=True)

        for key, value in updates.items():

            if not hasattr(new_state, key):
                raise ValueError(
                    f"未知状态字段: {key}"
                )

            setattr(new_state, key, value)

        new_state.version += 1

        return new_state