from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import crud, schemas
from agent.tools import follow_up_tool

router = APIRouter(
    prefix="/hcps",
    tags=["HCPs"]
)


@router.get("/", response_model=List[schemas.HCPResponse])
def get_hcps(
    db: Session = Depends(get_db)
):
    return crud.get_all_hcps(db)

@router.get("/search", response_model=List[schemas.HCPResponse])
def search_hcp(
    name: str,
    db: Session = Depends(get_db)
):
    return crud.search_hcps_by_name(db, name)


# @router.get(
#     "/{hcp_id}/history",
#     response_model=list[schemas.InteractionResponse]
# )
# def get_hcp_history(
#     hcp_id: int,
#     db: Session = Depends(get_db)
# ):

#     return crud.get_interaction_history(
#         db,
#         hcp_id
#     )

# @router.get(
#     "/followups",
#     response_model=dict
# )
# def get_followups(
#     db: Session = Depends(get_db)
# ):

#     return follow_up_tool(db)