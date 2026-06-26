from fastapi import FastAPI
from app.api.document_routes import router as document_router
from app.api.search_routes import (router as search_router)
from app.api.monitoring_routes import (router as monitoring_router)
from app.api.incident_routes import (router as incident_router)
from app.api.report_routes import (router as report_router)
from app.api.prometheus_routes import (router as prometheus_router)
from app.api.copilot_routes import (router as copilot_router)
from app.database.database import Base, engine
from app.models.incident import Incident
from app.api.history_routes import router as history_router





import app
from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version
)

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(document_router)
app.include_router(search_router)
app.include_router(monitoring_router)
app.include_router(incident_router)
app.include_router(report_router)
app.include_router(prometheus_router)
app.include_router(copilot_router)
app.include_router(history_router)

