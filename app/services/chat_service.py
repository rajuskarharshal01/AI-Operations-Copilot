from app.services.vector_service import retrieve_context
from app.services.prometheus_service import get_system_metrics
from app.services.llm_service import generate_llm_response
from app.services.monitoring_service import get_top_memory_processes
from app.services.history_service import get_recent_incidents
from app.services.monitoring_service import get_system_metrics as get_local_metrics


def chat_with_copilot(question: str):

    # Current live metrics
    try:
        metrics = get_system_metrics()

    except Exception:

        print("Prometheus unavailable. Falling back to local monitoring.")

        local = get_local_metrics()

        metrics = {
            "cpu_percent": local["metrics"]["cpu_percent"],
            "memory_percent": local["metrics"]["memory_percent"]
       }

    # Top memory consuming processes
    processes = get_top_memory_processes()

    # Relevant documentation from vector database
    context = retrieve_context(question)

    # Previous incidents from SQLite
    history = get_recent_incidents()

    # Format top processes
    process_text = "\n".join(
        [
            f"{process['name']} - {process['memory_mb']} MB"
            for process in processes
        ]
    )

    # Format historical incidents
    history_text = "\n".join(
        [
            (
                f"Time: {incident.timestamp}\n"
                f"CPU: {incident.cpu_percent}%\n"
                f"Memory: {incident.memory_percent}%\n"
                f"Severity: {incident.severity}\n"
                f"Top Process: {incident.top_process}\n"
                f"Summary: {incident.summary}\n"
            )
            for incident in history
        ]
    )

    prompt = f"""
You are an expert Site Reliability Engineer (SRE) and AI Operations Copilot.

Your job is to analyze:

1. Live infrastructure metrics
2. Top memory consuming processes
3. Previous incidents
4. Internal documentation

Use ALL available information before answering.

Current Infrastructure Metrics
------------------------------
CPU Usage: {metrics['cpu_percent']}%
Memory Usage: {metrics['memory_percent']}%

Top Memory Processes
--------------------
{process_text}

Previous Incidents
------------------
{history_text}

Relevant Documentation
----------------------
{context}

User Question
-------------
{question}

Instructions
------------
1. Analyze the current metrics first.
2. Compare them with previous incidents if relevant.
3. Mention recurring patterns when applicable.
4. Use the documentation only if it helps answer the question.
5. Never invent metrics or incidents.
6. If the system is healthy, clearly state that.
7. Keep the answer under 250 words.
8. Finish with a recommendation.

Answer:
"""

    answer = generate_llm_response(prompt)

    return {
        "question": question,
        "answer": answer
    }