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