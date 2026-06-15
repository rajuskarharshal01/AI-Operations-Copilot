import psutil
from datetime import datetime

def get_system_metrics():

   
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk =  psutil.disk_usage('/').percent
    
    issues = []

    if cpu > 80:
        issues.append("High CPU usage detected")

    if memory > 90:
        issues.append("High memory usage detected")

    if disk > 90:
        issues.append("Disk usage above 90%")


    status = "healthy"

    if issues:
        status = "issues detected"

    

    return {
        "status": status,
        "timestamp": datetime.utcnow().isoformat(),
        "metrics": {
            "cpu_percent": cpu,
            "memory_percent": memory,
            "disk_percent": disk
        },
        "issues": issues
    }


def get_top_processes(limit: int = 5):

    processes = []

    for proc in psutil.process_iter(
        ["pid", "name", "memory_info"]
    ):

        try:

            memory_mb = (
                proc.info["memory_info"].rss
                / 1024 / 1024
            )

            processes.append({
                "pid": proc.info["pid"],
                "name": proc.info["name"],
                "memory_mb": round(memory_mb, 2)
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    processes.sort(
        key=lambda x: x["memory_mb"],
        reverse=True
    )

    return processes[:limit]