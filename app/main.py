from fastapi import FastAPI
from app.api.document_routes import router as document_router
from app.api.search_routes import (router as search_router)
from app.api.monitoring_routes import (router as monitoring_router)
from app.api.incident_routes import (router as incident_router)
from app.api.report_routes import (router as report_router)




import app
from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version
)

app.include_router(router)
app.include_router(document_router)
app.include_router(search_router)
app.include_router(monitoring_router)
app.include_router(incident_router)
app.include_router(report_router)