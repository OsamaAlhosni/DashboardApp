from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="DashboardApp API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/metrics/")
def get_metrics():
    return {
        "total_users": 1420,
        "active_sessions": 312,
        "system_health": "Healthy"
    }

@app.get("/api/logs/")
def get_logs():
    return [
        {"timestamp": "2026-03-30 10:00:00", "level": "INFO", "message": "System started successfully."},
        {"timestamp": "2026-03-30 10:05:22", "level": "WARNING", "message": "High memory usage detected."},
        {"timestamp": "2026-03-30 10:12:45", "level": "INFO", "message": "User login successful."}
    ]
