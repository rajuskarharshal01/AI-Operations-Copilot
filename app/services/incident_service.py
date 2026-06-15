def analyze_system_health(metrics, processes):

    recommendations = []

    memory_percent = metrics["metrics"]["memory_percent"]
    cpu_percent = metrics["metrics"]["cpu_percent"]
    disk_percent = metrics["metrics"]["disk_percent"]

    if memory_percent > 80:

        top_process = processes[0]

        recommendations.append(
            f"High memory usage detected ({memory_percent}%)."
        )

        recommendations.append(
            f"Top memory consumer is "
            f"{top_process['name']} "
            f"using {top_process['memory_mb']} MB."
        )

        recommendations.append(
            "Investigate memory-intensive applications."
        )

    if cpu_percent > 80:

        recommendations.append(
            f"High CPU usage detected ({cpu_percent}%)."
        )

    if disk_percent > 90:

        recommendations.append(
            f"Disk usage exceeds 90% ({disk_percent}%)."
        )

    if not recommendations:

        recommendations.append(
            "System health appears normal."
        )

    return recommendations