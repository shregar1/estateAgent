from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from agent.state import AgentState

from constants.prompt import PromptConstant


class GraphNodes:

    @staticmethod
    def router_agent(state: AgentState) -> AgentState:
        """Determine which agent should handle a query"""
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
        
        # Create system message
        messages = [SystemMessage(content=PromptConstant.ROUTER_PROMPT)]
        
        # Add user message content
        last_message = state.messages[-1]
        
        if state.image_data:
            # If there's an image, we'll use the Issue Detection Agent
            state.next_agent = "issue_detection"
            return state
        
        # Get routing decision from LLM
        messages.append(last_message)
        response = llm.invoke(messages)
        response_text = response.content.strip()
        
        # Process the response
        if response_text.startswith("CLARIFY:"):
            # Send clarification back to user
            state.messages.append(AIMessage(content=response_text[8:].strip()))
            state.next_agent = "end"
        elif "issue_detection" in response_text.lower():
            state.next_agent = "issue_detection"
        elif "tenancy_faq" in response_text.lower():
            state.next_agent = "tenancy_faq"
        else:
            # Default response if classification fails
            state.messages.append(AIMessage(
                content="I'm not sure which type of question you're asking. Could you clarify if you're asking about a property issue or a tenancy question?"
            ))
            state.next_agent = "end"
        
        return state

    @staticmethod
    def issue_detection_agent(state: AgentState) -> AgentState:
        """Handle property issue detection and troubleshooting"""
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
        
        # Prepare message content
        messages = [SystemMessage(content=PromptConstant.ISSUE_DETECTION_PROMPT)]
        
        # Add conversation history (except the last message which we'll reconstruct)
        for msg in state.messages[:-1]:
            messages.append(msg)
        
        # Prepare the last user message with image if available
        last_user_message = state.messages[-1]
        content = []
        
        if isinstance(last_user_message.content, str):
            content.append({"type": "text", "text": last_user_message.content})
        else:
            # Handle case where content might already be a list
            for item in last_user_message.content:
                if isinstance(item, dict) and item.get("type") == "text":
                    content.append(item)
        
        # Add image if present
        if state.image_data:
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{state.image_data}"
                }
            })
        
        # Create a new message with both text and image
        image_message = HumanMessage(content=content)
        messages.append(image_message)
        
        # Get response
        response = llm.invoke(messages)
        
        # Add AI response to state
        state.messages.append(AIMessage(content=response.content))
        state.next_agent = "end"
        
        return state

    @staticmethod
    def tenancy_faq_agent(state: AgentState) -> AgentState:
        """Handle tenancy and rental questions"""
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
        
        # Prepare messages
        messages = [SystemMessage(content=PromptConstant.TENANCY_FAQ_PROMPT)]
        
        # Add all messages from history
        for msg in state.messages:
            messages.append(msg)
        
        # Get response
        response = llm.invoke(messages)
        
        # Add AI response to state
        state.messages.append(AIMessage(content=response.content))
        state.next_agent = "end"
        
        return state
