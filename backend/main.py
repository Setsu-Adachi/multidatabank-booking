from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Multibank Booking API")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "West Midlands Multibank API", "status": "running"}

@app.get("/api/slots")
def get_slots():
    """Get all available booking slots"""
    # Placeholder - will connect to database later
    return {
        "slots": [
            {
                "id": 1,
                "date": "2026-02-17",
                "time_start": "09:15",
                "time_end": "10:00",
                "capacity": 4,
                "booked": 2,
                "available": 2
            },
            {
                "id": 2,
                "date": "2026-02-17",
                "time_start": "10:00",
                "time_end": "10:45",
                "capacity": 4,
                "booked": 4,
                "available": 0
            },
            {
                "id": 3,
                "date": "2026-02-17",
                "time_start": "10:45",
                "time_end": "11:30",
                "capacity": 4,
                "booked": 1,
                "available": 3
            }
        ]
    }

@app.get("/api/stock")
def get_stock():
    """Get current stock availability"""
    return {
        "stock": [
            {"id": 1, "name": "Toothpaste", "available": True},
            {"id": 2, "name": "Hand Sanitiser", "available": True},
            {"id": 3, "name": "Cleaning Products", "available": True},
            {"id": 4, "name": "Baby Clothes", "available": True},
            {"id": 5, "name": "Toys", "available": False},
            {"id": 6, "name": "Electrical / Bulbs", "available": False},
        ]
    }

# Serve frontend files
frontend_path = Path(__file__).parent.parent / "frontend"
if frontend_path.exists():
    app.mount("/app", StaticFiles(directory=str(frontend_path), html=True), name="frontend")
    
    @app.get("/app")
    def serve_frontend():
        return FileResponse(str(frontend_path / "index.html"))
