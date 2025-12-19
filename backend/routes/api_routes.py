from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import API
from models import HealthLog

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/register")
def register_api(api: dict, db: Session = Depends(get_db)):
    new_api = API(
        name=api["name"],
        url=api["url"],
        method=api["method"]
    )
    db.add(new_api)
    db.commit()
    return {"message": "API registered successfully"}

@router.get("/api/status")
def get_api_status(db: Session = Depends(get_db)):
    apis = db.query(API).all()

    result = []
    for api in apis:
        result.append({
            "id": api.id,
            "name": api.name,
            "url": api.url,
            "method": api.method,
            "status": api.status
        })

    return result

@router.get("/api/logs")
def get_health_logs(db: Session = Depends(get_db)):
    logs = db.query(HealthLog).order_by(HealthLog.checked_at.desc()).limit(50).all()

    return [
        {
            "api_id": log.api_id,
            "status": log.status,
            "checked_at": log.checked_at
        }
        for log in logs
    ]