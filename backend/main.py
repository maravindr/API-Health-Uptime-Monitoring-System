from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes.api_routes import router
from scheduler import start_scheduler

app = FastAPI(title="API Health Monitoring System")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (ok for hackathon)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(router)

start_scheduler()

@app.get("/")
def root():
    return {"status": "API Monitor running"}
