from enum import Enum


class InteractionType(str, Enum):
    FACE_TO_FACE = "Face to Face"
    PHONE_CALL = "Phone Call"
    VIRTUAL_MEETING = "Virtual Meeting"
    EMAIL = "Email"


class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEUTRAL = "Neutral"
    NEGATIVE = "Negative"