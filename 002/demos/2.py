from pydantic import BaseModel
from typing import List


class AgentConfig(BaseModel):

    name: str

    tools: List[str]

    temperature: float


config = AgentConfig(
    name="ResearchAgent",
    tools=["search", "browser"],
    temperature=0.2
)

new_config = config.model_copy(deep=True)

new_config.tools.append("calculator")

print("原配置:", config.tools)

print("新配置:", new_config.tools)