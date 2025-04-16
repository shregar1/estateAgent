from langchain_core.messages.base import BaseMessage
from pydantic import BaseModel, Field
from typing import Optional, List
from typing_extensions import Annotated


class AgentState(BaseModel):
    """
    State model for the agent workflow.
    Fields:
        messages: Conversation history as a list of LangChain BaseMessage objects (supports multiple updates per step).
        next_agent: The name of the next agent node to route to.
        session_id: Unique identifier for the user session.
        image_data: Optional base64-encoded image data for property issue detection.
    """

    messages: Annotated[List[BaseMessage], 'langgraph:multiple'] = Field(default_factory=list)
    next_agent: Optional[str] = None
    session_id: str = ""
    image_data: Optional[str] = None