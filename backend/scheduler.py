import requests
import time
from apscheduler.schedulers.background import BackgroundScheduler
from database import SessionLocal
from models import API
from models import API, HealthLog


def check_apis():
    db = SessionLocal()
    apis = db.query(API).all()

    for api in apis:
        try:
            start = time.time()
            response = requests.request(api.method, api.url, timeout=5)
            response_time = round(time.time() - start, 2)

            if response.status_code < 300:
                api.status = "UP"
            else:
                api.status = "DOWN"

        except Exception:
            api.status = "DOWN"
        log = HealthLog(
        api_id=api.id,
        status=api.status
            )
        db.add(log)

        db.commit()

    db.close()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_apis, "interval", minutes=1)
    scheduler.start()
