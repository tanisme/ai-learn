from app.models.agent_state import (
    AgentState,
    ResearchResult
)


class ResearchAgent:
    """
    研究 Agent
    """

    def execute(
        self,
        state: AgentState
    ) -> dict:

        result = ResearchResult(
            title="Agent Architecture",
            content="Agent architecture research result",
            metadata={
                "source": "internal",
                "score": 0.95
            }
        )

        # 返回更新，不直接修改原 State
        return {
            "research_results": [
                *state.research_results,
                result
            ]
        }