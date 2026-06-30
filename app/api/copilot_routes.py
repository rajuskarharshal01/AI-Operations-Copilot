from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.chat_service import chat_with_copilot

from app.services.copilot_service import (
    generate_copilot_analysis
)

router = APIRouter(
    prefix="/copilot",
    tags=["Operations Copilot"]
)


@router.get("/analyze")
async def analyze():

    return generate_copilot_analysis()


@router.post("/chat")
async def chat(request: ChatRequest):

    return chat_with_copilot(request.question)