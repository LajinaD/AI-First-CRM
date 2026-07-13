from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from agent.graph import graph

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = graph.invoke({

        "message": request.message,

        "intent": "",

        "response": ""

    })

    return ChatResponse(
        response=result["response"]
    )