from fastapi import APIRouter

from app.services.monitoring_service import (
    get_system_metrics,
    get_top_memory_processes
)

from app.services.incident_service import (
    analyze_system_health
)

router = APIRouter(
    prefix="/incident",
    tags=["Incident Analysis"]
)


@router.get("/analyze")
async def analyze():

    metrics = get_system_metrics()

    processes = get_top_memory_processes()

    recommendations = analyze_system_health(
        metrics,
        processes
    )

    return {
        "metrics": metrics,
        "top_processes": processes,
        "analysis": recommendations
    }