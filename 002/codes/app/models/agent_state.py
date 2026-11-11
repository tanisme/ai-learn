from typing import List, Dict, Any

from pydantic import BaseModel, Field


class ResearchResult(BaseModel):
    """
    研究结果模型
    """

    title: str

    content: str

    metadata: Dict[str, Any] = Field(
        default_factory=dict
    )


class AgentState(BaseModel):
    """
    Agent 执行状态
    """

    task_id: str

    messages: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    research_results: List[ResearchResult] = Field(
        default_factory=list
    )

    summary: str = ""

    version: int = 1