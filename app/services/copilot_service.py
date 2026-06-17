from app.services.prometheus_service import (
    get_system_metrics
)

from app.services.monitoring_service import (
    get_top_processes
)

from app.services.incident_service import (
    analyze_system_health
)


def generate_copilot_analysis():

    metrics = get_system_metrics()

    processes = get_top_processes()

    analysis = analyze_system_health(
        {
            "metrics": {
                "cpu_percent":
                    metrics["cpu_percent"],
                "memory_percent":
                    metrics["memory_percent"],
                "disk_percent": 0
            }
        },
        processes
    )

    return {
        "overall_status":
            metrics["status"],

        "cpu_percent":
            metrics["cpu_percent"],

        "memory_percent":
            metrics["memory_percent"],

        "top_process":
            processes[0]["name"],

        "analysis":
            analysis
    }