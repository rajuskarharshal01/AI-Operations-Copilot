from fastapi import FastAPI

app = FastAPI(
    title="AI Operations Copilot",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Operations Copilot API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }