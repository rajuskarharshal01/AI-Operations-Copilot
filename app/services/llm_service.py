from ollama import chat
import ollama


def generate_incident_explanation(cpu, memory, top_process, analysis):

    prompt = f"""
You are an experienced Site Reliability Engineer.

Current Metrics

CPU Usage: {cpu}%
Memory Usage: {memory}%

Top Process:
{top_process}

Analysis:
{analysis}

Provide:

1. Incident Summary
2. Likely Cause
3. Recommended Action
"""

    return generate_llm_response(prompt)


def generate_llm_response(prompt: str):

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]