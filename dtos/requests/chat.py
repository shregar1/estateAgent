from pydantic import BaseModel


class ChatResponseDTO(BaseModel):
    message: str
    session_id: str
    agent_name: str