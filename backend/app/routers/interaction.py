from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from agent.tools import follow_up_tool
from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)


@router.post(
    "/",
    response_model=schemas.InteractionResponse
)
def create_interaction_endpoint(
    interaction: schemas.InteractionCreate,
    db: Session = Depends(get_db),
):
    return crud.create_interaction(db, interaction)


@router.get(
    "/",
    response_model=List[schemas.InteractionResponse]
)
def get_all_interactions(
    db: Session = Depends(get_db),
):
    return crud.get_all_interactions(db)

@router.get(
    "/history/{hcp_id}",
    response_model=List[schemas.InteractionResponse]
)
def get_interaction_history(
    hcp_id: int,
    db: Session = Depends(get_db),
):
    return crud.get_interaction_history(db, hcp_id)


@router.get("/followups")
def get_followups(
    db: Session = Depends(get_db),
):
    return follow_up_tool(db)