from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Customer Support Automation System",
    version="1.0.0",
    description="Multi-Agent AI Customer Support Platform"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "AI Customer Support Automation System Running"
    }
