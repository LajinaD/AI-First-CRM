from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Time,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    specialization = Column(String(255))

    hospital = Column(String(255))

    city = Column(String(255))

    interactions = relationship(
        "Interaction",
        back_populates="hcp"
    )


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_id = Column(
        Integer,
        ForeignKey("hcps.id"),
        nullable=False
    )

    interaction_type = Column(
        String(100),
        nullable=False
    )

    interaction_date = Column(
        Date,
        nullable=False
    )

    interaction_time = Column(
        Time,
        nullable=False
    )

    attendees = Column(Text)

    topics_discussed = Column(Text)

    materials_shared = Column(Text)

    samples_distributed = Column(Text)

    sentiment = Column(String(20))

    outcomes = Column(Text)

    follow_up_actions = Column(Text)

    ai_summary = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    hcp = relationship(
        "HCP",
        back_populates="interactions"
    )