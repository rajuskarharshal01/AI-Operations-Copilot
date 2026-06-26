from fastapi import APIRouter

from app.services.history_service import save_incident
from app.services.history_service import (save_incident, get_all_incidents)
from app.services.history_service import (save_incident, get_all_incidents, get_latest_incident, delete_history)

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

@router.post("/test")
def test_save():

    incident = save_incident(
        cpu_percent=10.5,
        memory_percent=42.7,
        severity="healthy",
        top_process="chrome.exe",
        summary="System operating normally."
    )

    return {
        "message": "Incident saved",
        "id": incident.id
    }

@router.get("")
def get_history():

    incidents = get_all_incidents()

    return incidents


@router.get("/latest")
def latest():

    return get_latest_incident()


@router.delete("")
def clear_history():

    delete_history()

    return {
        "message": "History deleted successfully."
    }