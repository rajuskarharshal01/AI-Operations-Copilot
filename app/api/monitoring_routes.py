from fastapi import APIRouter

from app.services.monitoring_service import (get_system_metrics, get_top_processes)


router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring"]
)

@router.get("/system")
async def system_metrics():
    return get_system_metrics()


@router.get("/processes")
async def top_processes():

    return {
        "top_memory_processes":
            get_top_processes()
    }