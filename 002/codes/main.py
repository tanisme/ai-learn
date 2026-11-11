from app.models.agent_state import AgentState

from app.core.state_manager import StateManager

from app.agents.research_agent import ResearchAgent

from app.agents.summary_agent import SummaryAgent


def main():

    # 1. 创建初始状态
    state = AgentState(
        task_id="task-001"
    )

    print("初始版本:", state.version)

    # 2. Research Agent 执行
    research_agent = ResearchAgent()

    research_updates = research_agent.execute(
        state
    )

    # 3. 更新状态
    state = StateManager.update(
        state,
        research_updates
    )

    print("研究完成:", len(state.research_results))

    # 4. Summary Agent 执行
    summary_agent = SummaryAgent()

    summary_updates = summary_agent.execute(
        state
    )

    # 5. 再次更新状态
    state = StateManager.update(
        state,
        summary_updates
    )

    print("摘要:", state.summary)

    # 6. 验证深拷贝
    new_state = StateManager.deep_copy(state)

    print(
        "是否为同一个对象:",
        state is new_state
    )

    print(
        "研究结果列表是否共享:",
        state.research_results is new_state.research_results
    )

    print("最终版本:", state.version)


if __name__ == "__main__":
    main()