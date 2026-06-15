from fastapi import APIRouter

from app.services.monitoring_service import (get_system_metrics)


router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring"]
)

@router.get("/system")
async def system_metrics():
    return get_system_metrics()