from agent.state import CRMState
from services.groq_service import get_llm

from app.database import SessionLocal
from agent.tools import (
    log_interaction_tool,
    edit_interaction_tool,
    search_hcp_tool,
    interaction_history_tool,
    follow_up_tool,
    extract_doctor_name
)


llm = get_llm()


def classify_intent_node(state: CRMState):

    prompt = f"""
You are an AI assistant for a Healthcare CRM.

Classify the user's request into ONLY ONE of these categories.

Categories:

- log_interaction
- edit_interaction
- fetch_hcp
- interaction_history
- follow_up
- general_chat

Examples:

"I met Dr Rahul Sharma today"
→ log_interaction

"Change the sentiment of Dr Rahul Sharma to Neutral"
→ edit_interaction

"Find Dr Rahul Sharma"
→ fetch_hcp

"Show interaction history of Dr Rahul Sharma"
→ interaction_history

"Who needs follow up?"
→ follow_up

"Hello"
→ general_chat

Return ONLY the category.

User:
{state["message"]}
"""

    result = llm.invoke(prompt)

    state["intent"] = result.content.strip().lower()

    return state


def general_chat_node(state: CRMState):

    response = llm.invoke(state["message"])

    state["response"] = response.content

    return state


def log_node(state: CRMState):

    db = SessionLocal()

    result = log_interaction_tool(
        db,
        state["message"]
    )

    db.close()

    state["tool_result"] = result
    state["response"] = result["message"]

    return state

def edit_node(state: CRMState):

    db = SessionLocal()

    result = edit_interaction_tool(
        db,
        state["message"]
    )

    db.close()

    state["tool_result"] = result
    state["response"] = result["message"]

    return state

def search_node(state: CRMState):

    db = SessionLocal()

    extracted = extract_doctor_name(state["message"])

    doctor = extracted.doctor_name

    result = search_hcp_tool(
        db,
        doctor
    )

    db.close()

    state["tool_result"] = result

    state["response"] = str(result)

    return state


def history_node(state: CRMState):

    db = SessionLocal()

    extracted = extract_doctor_name(state["message"])

    doctor = extracted.doctor_name

    result = interaction_history_tool(
        db,
        doctor
    )

    db.close()

    state["tool_result"] = result

    state["response"] = str(result)

    return state

def followup_node(state: CRMState):

    db = SessionLocal()

    result = follow_up_tool(db)

    db.close()

    state["tool_result"] = result

    state["response"] = str(result)

    return state