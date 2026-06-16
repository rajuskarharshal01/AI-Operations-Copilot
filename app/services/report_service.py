def generate_incident_report(metrics, processes, analysis):

    memory = metrics["metrics"]["memory_percent"]
    cpu = metrics["metrics"]["cpu_percent"]
    disk = metrics["metrics"]["disk_percent"]

    severity = "healthy"

    if memory > 80:
        severity = "warning"

    if memory > 90 or disk > 90:
        severity = "critical"

    top_process = processes[0]

    summary = (
        f"System memory utilization is "
        f"{memory}%. "
        f"The highest memory consumer is "
        f"{top_process['name']} "
        f"using {top_process['memory_mb']} MB. "
        f"CPU utilization is {cpu}% "
        f"and disk utilization is {disk}%."
    )

    return {
        "severity": severity,
        "summary": summary,
        "recommendations": analysis
    }

