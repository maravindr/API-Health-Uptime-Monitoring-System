from fastapi import FastAPI
from database import Base, engine
from routes.api_routes import router
from scheduler import start_scheduler

app = FastAPI(title="API Health Monitoring System")

Base.metadata.create_all(bind=engine)
app.include_router(router)

start_scheduler()

@app.get("/")
def root():
    return {"status": "API Monitor running"}
