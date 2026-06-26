from fastapi import APIRouter

from app.services.monitoring_service import (get_system_metrics, get_top_memory_processes)

from app.services.history_service import save_incident
from app.services.incident_service import (analyze_system_health)

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

    severity = "healthy"

    if metrics["metrics"]["cpu_percent"] > 80 or metrics["metrics"]["memory_percent"] > 80:
        severity = "warning"

    if metrics["metrics"]["cpu_percent"] > 90 or metrics["metrics"]["memory_percent"] > 90:
        severity = "critical"


    save_incident(
        cpu_percent=metrics["metrics"]["cpu_percent"],
        memory_percent=metrics["metrics"]["memory_percent"],
        severity=severity,
        top_process=processes[0]["name"],
        summary=" ".join(recommendations)
)

    return {
        "metrics": metrics,
        "top_processes": processes,
        "analysis": recommendations
    }