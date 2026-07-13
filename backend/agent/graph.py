from langgraph.graph import StateGraph, START, END

from agent.state import CRMState
from agent.nodes import (
    classify_intent_node,
    general_chat_node,
    log_node,
    edit_node,
    search_node,
    history_node,
    followup_node,
)

builder = StateGraph(CRMState)

# Nodes
builder.add_node("classify", classify_intent_node)
builder.add_node("log", log_node)
builder.add_node("edit", edit_node)
builder.add_node("search", search_node)
builder.add_node("history", history_node)
builder.add_node("followup", followup_node)
builder.add_node("chat", general_chat_node)

builder.add_edge(START, "classify")


def route(state: CRMState):

    intent = state["intent"]

    if intent == "log_interaction":
        return "log"

    elif intent == "edit_interaction":
        return "edit"

    elif intent == "fetch_hcp":
        return "search"

    elif intent == "interaction_history":
        return "history"

    elif intent == "follow_up":
        return "followup"

    return "chat"


builder.add_conditional_edges(
    "classify",
    route,
    {
        "log": "log",
        "edit": "edit",
        "search": "search",
        "history": "history",
        "followup": "followup",
        "chat": "chat",
    },
)

builder.add_edge("log", END)
builder.add_edge("edit", END)
builder.add_edge("search", END)
builder.add_edge("history", END)
builder.add_edge("followup", END)
builder.add_edge("chat", END)

graph = builder.compile()

