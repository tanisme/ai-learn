import pytest

from app.generators import generate_tokens


@pytest.mark.asyncio
async def test_generate_tokens():

    result = []

    async for token in generate_tokens(
        "Hello World",
        delay=0
    ):

        result.append(token)

    assert result == [
        "Hello ",
        "World"
    ]


@pytest.mark.asyncio
async def test_empty_text():

    result = []

    async for token in generate_tokens(
        "",
        delay=0
    ):

        result.append(token)

    assert result == [""]


@pytest.mark.asyncio
async def test_negative_delay():

    with pytest.raises(ValueError):

        async for _ in generate_tokens(
            "Hello",
            delay=-1
        ):
            pass