from ollama import chat


def generate_incident_explanation(
    cpu_percent,
    memory_percent,
    top_process,
    analysis
):

    prompt = f"""
    You are an AI Operations Engineer.

    CPU Usage: {cpu_percent}%
    Memory Usage: {memory_percent}%

    Top Process:
    {top_process}

    Findings:
    {analysis}

    Generate:
    1. Incident Summary
    2. Likely Cause
    3. Recommended Action

    Keep the response concise.
    """

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]