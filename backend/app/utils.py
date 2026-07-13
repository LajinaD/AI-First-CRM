from datetime import datetime, date

from app.enums import InteractionType, Sentiment


def parse_date(value: str) -> date:
    value = value.lower().strip()

    if value == "today":
        return date.today()

    if value == "yesterday":
        return date.fromordinal(date.today().toordinal() - 1)

    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except:
        return date.today()


def parse_time(value: str):
    try:
        return datetime.strptime(value, "%I %p").time()
    except:
        return datetime.strptime("09:00 AM", "%I:%M %p").time()


# NEW FUNCTION
def map_interaction_type(value: str) -> InteractionType:
    if not value:
        return InteractionType.FACE_TO_FACE

    mapping = {
        "face to face": InteractionType.FACE_TO_FACE,
        "meeting": InteractionType.FACE_TO_FACE,
        "phone call": InteractionType.PHONE_CALL,
        "virtual meeting": InteractionType.VIRTUAL_MEETING,
        "email": InteractionType.EMAIL,
    }

    return mapping.get(
        value.lower().strip(),
        InteractionType.FACE_TO_FACE
    )


# NEW FUNCTION
def map_sentiment(value: str | None) -> Sentiment | None:
    if not value:
        return None

    mapping = {
        "positive": Sentiment.POSITIVE,
        "neutral": Sentiment.NEUTRAL,
        "negative": Sentiment.NEGATIVE,
    }

    return mapping.get(value.lower().strip())