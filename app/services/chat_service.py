from app.services.vector_service import retrieve_context
from app.services.prometheus_service import get_system_metrics
from app.services.llm_service import generate_llm_response
from app.services.monitoring_service import get_top_memory_processes

def chat_with_copilot(question: str):

    metrics = get_system_metrics()
    processes = get_top_memory_processes()

    context = retrieve_context(question)

    process_text = "\n".join(
        [
            f"{process['name']} - {process['memory_mb']} MB"
            for process in processes
        ]
    )

    prompt = f"""
You are an expert Site Reliability Engineer (SRE).

You MUST answer ONLY using the information provided below.
Do NOT assume any values.
Do NOT invent metrics.
If the metrics show the system is healthy, explicitly say so.

Current Infrastructure Metrics
------------------------------
CPU Usage: {metrics['cpu_percent']}%
Memory Usage: {metrics['memory_percent']}%

Top Memory Processes
--------------------
{process_text}

Relevant Documentation
----------------------
{context}

User Question
-------------
{question}

Instructions
------------
1. First analyze the metrics.
2. Mention the top memory consuming process if relevant.
3. If CPU or memory is not high, clearly state that.
4. Use the documentation only if it is relevant.
5. Keep the answer under 200 words.
6. End with a recommendation.

Answer:
"""

    answer = generate_llm_response(prompt)

    return answer