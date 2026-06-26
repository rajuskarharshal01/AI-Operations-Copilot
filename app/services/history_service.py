from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.incident import Incident

def save_incident(
    cpu_percent: float,
    memory_percent: float,
    severity: str,
    top_process: str,
    summary: str
):
    
    db: Session = SessionLocal()

    try:

        incident = Incident(
            cpu_percent=cpu_percent,
            memory_percent=memory_percent,
            severity=severity,
            top_process=top_process,
            summary=summary
        )

        db.add(incident)
        db.commit()
        db.refresh(incident)

        return incident

    finally:

        db.close()

def get_all_incidents():

    db = SessionLocal()

    try:

        incidents = (
            db.query(Incident)
            .order_by(Incident.timestamp.desc())
            .all()
        )

        return incidents

    finally:

        db.close()


def get_latest_incident():

    db = SessionLocal()

    try:

        incident = (
            db.query(Incident)
            .order_by(Incident.timestamp.desc())
            .first()
        )

        return incident

    finally:

        db.close()


def delete_history():

    db = SessionLocal()

    try:

        db.query(Incident).delete()

        db.commit()

    finally:

        db.close()