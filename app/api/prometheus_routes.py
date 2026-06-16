from fastapi import APIRouter
from app.services.prometheus_service import (query_prometheus)
from app.services.prometheus_service import (query_prometheus, get_cpu_usage)
from app.services.prometheus_service import (get_memory_usage)
from app.services.prometheus_service import (query_prometheus, get_cpu_usage, get_memory_usage, get_system_metrics)


router = APIRouter(
    prefix="/prometheus",
    tags=["Prometheus"]
)


@router.get("/health")
async def prometheus_health():

    result = query_prometheus("up")

    return result



@router.get("/cpu")
async def cpu_usage():

    return get_cpu_usage()


@router.get("/memory")
async def memory_usage():

    return get_memory_usage()


@router.get("/system")
async def system_metrics():

    return get_system_metrics()