import requests

PROMETHEUS_URL = "http://localhost:9090"


def query_prometheus(query: str):

    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": query}
    )

    return response.json()


def get_cpu_usage():

    query = (
        '100 - (avg by(instance) '
        '(rate(node_cpu_seconds_total'
        '{mode="idle"}[5m])) * 100)'
    )

    response = query_prometheus(query)

    value = float(
        response["data"]["result"][0]["value"][1]
    )

    return {
        "cpu_percent": round(value, 2)
    }


def get_memory_usage():

    query = (
        '(1 - (node_memory_MemAvailable_bytes '
        '/ node_memory_MemTotal_bytes)) * 100'
    )

    response = query_prometheus(query)

    value = float(
        response["data"]["result"][0]["value"][1]
    )

    return {
        "memory_percent": round(value, 2)
    }


def get_system_metrics():

    cpu = get_cpu_usage()["cpu_percent"]

    memory = get_memory_usage()["memory_percent"]

    status = "healthy"

    if cpu > 80 or memory > 80:
        status = "warning"

    if cpu > 90 or memory > 90:
        status = "critical"

    return {
        "status": status,
        "cpu_percent": cpu,
        "memory_percent": memory
    }