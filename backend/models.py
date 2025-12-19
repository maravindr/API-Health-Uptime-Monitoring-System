from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import DateTime
from datetime import datetime
class API(Base):
    __tablename__ = "apis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String)
    method = Column(String)
    status = Column(String, default="UNKNOWN")

class HealthLog(Base):
    __tablename__ = "health_logs"

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(Integer)
    status = Column(String)
    checked_at = Column(DateTime, default=datetime.utcnow)