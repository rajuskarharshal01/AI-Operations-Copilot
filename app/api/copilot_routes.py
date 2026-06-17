from fastapi import APIRouter

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