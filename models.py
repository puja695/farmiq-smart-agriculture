from database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
import datetime

class CropData(Base):
    __tablename__ = "crop_data"

    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    date = Column(DateTime, default=datetime.datetime.utcnow)
