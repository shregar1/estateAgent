from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.nodes import GraphNodes
from config import logger
from typing import Any

class Graph:
    """
    Provides a static method to construct the agent workflow graph for the real estate assistant.
    """

    @staticmethod
    def create_agent_graph() -> Any:
        """
        Create the agent workflow graph with router, issue detection, and tenancy FAQ nodes.
        Returns the compiled LangGraph workflow.
        """

        logger.info("[Graph] Initializing agent workflow graph.")
        graph: StateGraph = StateGraph(AgentState)
        graph.add_node("router", GraphNodes.router_agent)
        graph.add_node("issue_detection", GraphNodes.issue_detection_agent)
        graph.add_node("tenancy_faq", GraphNodes.tenancy_faq_agent)
        logger.info("[Graph] Added agent nodes: router, issue_detection, tenancy_faq.")

        # Conditional routing from router
        graph.add_conditional_edges(
            "router",
            lambda state: state.next_agent,
            {
                "issue_detection": "issue_detection",
                "tenancy_faq": "tenancy_faq",
                "end": END
            }
        )
        logger.info("[Graph] Added conditional edges from router.")
        # After each agent, go to END
        graph.add_edge("issue_detection", END)
        graph.add_edge("tenancy_faq", END)
        logger.info("[Graph] Added END edges for issue_detection and tenancy_faq.")

        graph.set_entry_point("router")
        logger.info("[Graph] Set entry point to router.")
        compiled_graph = graph.compile()
        logger.info("[Graph] Agent workflow graph compiled and ready.")

        return compiled_graph