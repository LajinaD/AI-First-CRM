from datetime import date, time
from typing import Optional
from app.enums import InteractionType, Sentiment
from pydantic import BaseModel


class HCPBasic(BaseModel):
    id: int
    name: str
    specialization: str | None = None
    hospital: str | None = None
    
    class Config:
        from_attributes = True


class InteractionCreate(BaseModel):
    hcp_id: int

    interaction_type: InteractionType

    interaction_date: date

    interaction_time: time

    attendees: Optional[str] = None

    topics_discussed: Optional[str] = None

    materials_shared: Optional[str] = None

    samples_distributed: Optional[str] = None

    sentiment: Optional[Sentiment] = None

    outcomes: Optional[str] = None

    follow_up_actions: Optional[str] = None


class InteractionResponse(BaseModel):
    id: int

    hcp: HCPBasic

    interaction_type: InteractionType

    interaction_date: date

    interaction_time: time

    attendees: Optional[str] = None

    topics_discussed: Optional[str] = None

    materials_shared: Optional[str] = None

    samples_distributed: Optional[str] = None

    sentiment: Optional[Sentiment] = None

    outcomes: Optional[str] = None

    follow_up_actions: Optional[str] = None

    ai_summary: Optional[str] = None

    class Config:
        from_attributes = True


class HCPResponse(BaseModel):
    id: int
    name: str
    specialization: str | None = None
    hospital: str | None = None
    city: str | None = None

    class Config:
        from_attributes = True



class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


class FollowUpResponse(BaseModel):

    doctor: str

    date: date

    topic: str | None = None

    follow_up: str | None = None