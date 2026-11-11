import pytest

from app.agent import StreamingAgent


@pytest.mark.asyncio
async def test_agent_event_sequence():

    agent = StreamingAgent(
        token_delay=0
    )

    events = []

    async for event in agent.run(
        "请解释 Python"
    ):

        events.append(event)

    event_names = [
        event.event
        for event in events
    ]

    assert event_names[0] == "run_start"

    assert event_names[-1] == "done"

    assert "node_start" in event_names

    assert "node_end" in event_names

    assert "token" in event_names


@pytest.mark.asyncio
async def test_empty_prompt():

    agent = StreamingAgent(
        token_delay=0
    )

    events = []

    async for event in agent.run("   "):

        events.append(event)

    assert len(events) == 1

    assert events[0].event == "error"


@pytest.mark.asyncio
async def test_token_content():

    agent = StreamingAgent(
        token_delay=0
    )

    tokens = []

    async for event in agent.run("测试"):

        if event.event == "token":

            tokens.append(
                event.data["content"]
            )

    result = "".join(tokens)

    assert result == (
        "Python 生成器可以实现 "
        "高效的流式数据处理。"
    )