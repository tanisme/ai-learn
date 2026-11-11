from app.models.agent_state import AgentState


class SummaryAgent:
    """
    摘要 Agent
    """

    def execute(
        self,
        state: AgentState
    ) -> dict:

        count = len(state.research_results)

        titles = [
            item.title
            for item in state.research_results
        ]

        summary = (
            f"研究完成，共收集 {count} 条结果。"
            f"研究主题：{', '.join(titles)}"
        )

        return {
            "summary": summary
        }