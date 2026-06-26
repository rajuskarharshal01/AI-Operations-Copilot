from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base

class Incident(Base):

    __tablename__ = "incident_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    cpu_percent = Column(
        Float
    )

    memory_percent = Column(
        Float
    )

    severity = Column(
        String
    )

    top_process = Column(
        String
    )

    summary = Column(
        String
    )