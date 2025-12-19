from sqlalchemy import Column, Integer, String
from database import Base

class API(Base):
    __tablename__ = "apis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String)
    method = Column(String)
    status = Column(String, default="UNKNOWN")
