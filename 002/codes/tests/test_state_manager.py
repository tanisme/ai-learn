from app.models.agent_state import (
    AgentState,
    ResearchResult
)

from app.core.state_manager import StateManager


def create_state():

    return AgentState(
        task_id="task-001",
        research_results=[
            ResearchResult(
                title="Agent",
                content="Agent architecture",
                metadata={
                    "tags": ["AI", "Python"]
                }
            )
        ]
    )


def test_shallow_copy():

    state = create_state()

    new_state = StateManager.shallow_copy(
        state
    )

    assert state is not new_state

    # 浅拷贝共享嵌套列表
    assert (
        state.research_results
        is new_state.research_results
    )


def test_deep_copy():

    state = create_state()

    new_state = StateManager.deep_copy(
        state
    )

    assert state is not new_state

    assert (
        state.research_results
        is not new_state.research_results
    )

    assert (
        state.research_results[0]
        is not new_state.research_results[0]
    )


def test_update():

    state = create_state()

    new_state = StateManager.update(
        state,
        {
            "summary": "Research completed"
        }
    )

    assert state.summary == ""

    assert new_state.summary == "Research completed"

    assert new_state.version == state.version + 1


def test_nested_data_isolation():

    state = create_state()

    new_state = StateManager.deep_copy(
        state
    )

    new_state.research_results[0].metadata[
        "tags"
    ].append("Agent")

    assert (
        "Agent"
        not in state.research_results[0].metadata["tags"]
    )