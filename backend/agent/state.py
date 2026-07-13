from typing import TypedDict


class CRMState(TypedDict):
    message: str

    intent: str

    response: str

    tool_result: dict