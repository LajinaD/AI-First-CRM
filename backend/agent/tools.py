from pydantic import BaseModel
from typing import Optional
from services.groq_service import get_llm

from sqlalchemy.orm import Session

from app import crud, schemas

from app.utils import (
    parse_date,
    parse_time,
    map_interaction_type,
    map_sentiment,
)

llm = get_llm()


class InteractionExtraction(BaseModel):
    doctor_name: str

    interaction_type: Optional[str] = None

    interaction_date: Optional[str] = None

    interaction_time: Optional[str] = None

    attendees: Optional[str] = None

    topics_discussed: Optional[str] = None

    materials_shared: Optional[str] = None

    samples_distributed: Optional[str] = None

    sentiment: Optional[str] = None

    outcomes: Optional[str] = None

    follow_up_actions: Optional[str] = None


class EditInteractionExtraction(BaseModel):

    doctor_name: str

    field_name: str

    new_value: str

class DoctorSearchExtraction(BaseModel):
    doctor_name: str


def extract_interaction(message: str):

    structured_llm = llm.with_structured_output(
        InteractionExtraction
    )

    prompt = f"""
You are an AI assistant for a Healthcare CRM.

Extract the interaction details from the user's message.

Rules:

- doctor_name should contain only the doctor's name.

- interaction_type must be ONLY one of:
  Face to Face
  Phone Call
  Virtual Meeting
  Email

- If the user says "met", assume "Face to Face".

- Keep the date exactly as mentioned
  (today, yesterday, Monday, etc.)

- Keep the time exactly as mentioned.

- If any field is missing, return null.

User Message:

{message}
"""

    return structured_llm.invoke(prompt)


def log_interaction_tool(db: Session, message: str):

    extracted = extract_interaction(message)

    # Find doctor in database
    hcp = crud.get_hcp_by_name(db, extracted.doctor_name)

    if not hcp:
        return {
            "success": False,
            "message": f"HCP '{extracted.doctor_name}' not found."
        }

    interaction = schemas.InteractionCreate(

        hcp_id=hcp.id,

        interaction_type=map_interaction_type(extracted.interaction_type),

        interaction_date=parse_date(extracted.interaction_date),

        interaction_time=parse_time(extracted.interaction_time),

        attendees=extracted.attendees,

        topics_discussed=extracted.topics_discussed,

        materials_shared=extracted.materials_shared,

        samples_distributed=extracted.samples_distributed,

        sentiment=map_sentiment(extracted.sentiment),

        outcomes=extracted.outcomes,

        follow_up_actions=extracted.follow_up_actions,
    )

    saved = crud.create_interaction(db, interaction)

    return {
        "success": True,
        "interaction_id": saved.id,
        "doctor": hcp.name,
        "message": "Interaction logged successfully."
    }


def search_hcp_tool(db: Session, doctor_name: str):

    hcps = crud.search_hcps(db, doctor_name)

    if not hcps:
        return {
            "success": False,
            "message": "No HCP found."
        }

    results = []

    for hcp in hcps:

        results.append({

            "id": hcp.id,

            "name": hcp.name,

            "specialization": hcp.specialization,

            "hospital": hcp.hospital,

            "city": hcp.city,

        })

    return {
        "success": True,
        "results": results
    }



def extract_edit_request(message: str):

    structured_llm = llm.with_structured_output(
        EditInteractionExtraction
    )

    prompt = f"""
You are an AI CRM assistant.

Extract:

- doctor_name
- field_name
- new_value

Example:

"Change sentiment of Dr Rahul Sharma to Neutral"

doctor_name = Dr Rahul Sharma
field_name = sentiment
new_value = Neutral

User:

{message}
"""

    return structured_llm.invoke(prompt)



from app.utils import map_sentiment


def edit_interaction_tool(db: Session, message: str):

    extracted = extract_edit_request(message)

    # Find the doctor
    hcp = crud.get_hcp_by_name(db, extracted.doctor_name)

    if not hcp:
        return {
            "success": False,
            "message": "Doctor not found."
        }

    # Get latest interaction
    interaction = crud.get_latest_interaction_by_hcp(
        db,
        hcp.id
    )

    if not interaction:
        return {
            "success": False,
            "message": "No interaction found."
        }

    # Update supported fields
    if extracted.field_name.lower() == "sentiment":
        interaction.sentiment = map_sentiment(
            extracted.new_value
        )

    elif extracted.field_name.lower() == "outcomes":
        interaction.outcomes = extracted.new_value

    elif extracted.field_name.lower() == "follow_up_actions":
        interaction.follow_up_actions = extracted.new_value

    else:
        return {
            "success": False,
            "message": f"Editing '{extracted.field_name}' is not supported yet."
        }

    crud.update_interaction(db, interaction)

    return {
        "success": True,
        "message": "Interaction updated successfully."
    }



def interaction_history_tool(db: Session, doctor_name: str):

    hcp = crud.get_hcp_by_name(db, doctor_name)

    if not hcp:
        return {
            "success": False,
            "message": "Doctor not found."
        }

    interactions = crud.get_interaction_history(db, hcp.id)

    history = []

    for interaction in interactions:

        history.append({

            "date": str(interaction.interaction_date),

            "type": interaction.interaction_type,

            "topic": interaction.topics_discussed,

            "sentiment": interaction.sentiment,

            "outcome": interaction.outcomes,

            "follow_up": interaction.follow_up_actions,

        })

    return {

        "success": True,

        "doctor": hcp.name,

        "history": history

    }


def follow_up_tool(db: Session):

    interactions = crud.get_follow_up_interactions(db)

    results = []

    for interaction in interactions:

        results.append({

            "doctor": interaction.hcp.name,

            "date": str(interaction.interaction_date),

            "follow_up": interaction.follow_up_actions,

            "topic": interaction.topics_discussed

        })

    return {

        "success": True,

        "results": results

    }



def extract_doctor_name(message: str):

    structured_llm = llm.with_structured_output(
        DoctorSearchExtraction
    )

    prompt = f"""
Extract only the doctor's name.

Examples:

Find Dr Rahul Sharma
→ Dr Rahul Sharma

Show interaction history of Dr Priya Mehta
→ Dr Priya Mehta

User:

{message}
"""

    return structured_llm.invoke(prompt)