from sqlalchemy.orm import Session,joinedload

from app import models, schemas


def create_interaction(
    db: Session,
    interaction: schemas.InteractionCreate,
):
    db_interaction = models.Interaction(
        **interaction.model_dump()
    )

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return (
        db.query(models.Interaction)
        .options(joinedload(models.Interaction.hcp))
        .filter(models.Interaction.id == db_interaction.id)
        .first()
    )


def get_all_hcps(db: Session):
    return db.query(models.HCP).all()


def get_all_interactions(db: Session):

    return (
        db.query(models.Interaction)
        .options(joinedload(models.Interaction.hcp))
        .order_by(models.Interaction.created_at.desc())
        .all()
    )


def get_hcp_by_name(db: Session, name: str):
    return (
        db.query(models.HCP)
        .filter(models.HCP.name.ilike(f"%{name}%"))
        .first()
    )


def search_hcps(db: Session, keyword: str):

    return (
        db.query(models.HCP)
        .filter(
            models.HCP.name.ilike(f"%{keyword}%")
        )
        .all()
    )


def get_latest_interaction_by_hcp(db: Session, hcp_id: int):
    return (
        db.query(models.Interaction)
        .filter(models.Interaction.hcp_id == hcp_id)
        .order_by(models.Interaction.created_at.desc())
        .first()
    )


def update_interaction(db: Session, interaction):

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


def get_interaction_history(db: Session, hcp_id: int):

    return (
        db.query(models.Interaction)
        .filter(models.Interaction.hcp_id == hcp_id)
        .order_by(models.Interaction.interaction_date.desc())
        .all()
    )

def get_follow_up_interactions(db: Session):

    return (
        db.query(models.Interaction)
        .filter(models.Interaction.follow_up_actions.isnot(None))
        .all()
    )


def get_all_hcps(db: Session):
    return db.query(models.HCP).all()


def search_hcps_by_name(db: Session, name: str):
    return (
        db.query(models.HCP)
        .filter(models.HCP.name.ilike(f"%{name}%"))
        .all()
    )