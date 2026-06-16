from fastapi import APIRouter
from app.services.monitoring_service import (get_system_metrics, get_top_processes)
from app.services.incident_service import (analyze_system_health)
from app.services.incident_service import (analyze_system_health)
from app.services.report_service import (generate_incident_report)

router = APIRouter(
    prefix="/report",
    tags=["Incident Reports"]
)

@router.get("/incident")
async def incident_report():

    metrics = get_system_metrics()

    processes = get_top_processes()

    analysis = analyze_system_health(
        metrics,
        processes
    )

    report = generate_incident_report(
        metrics,
        processes,
        analysis
    )

    return report



