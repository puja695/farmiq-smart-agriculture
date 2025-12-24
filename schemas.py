from pydantic import BaseModel
from datetime import datetime

# Base schema for crop data
class CropDataBase(BaseModel):
    crop_name: str
    location: str
    soil_moisture: float
    temperature: float
    humidity: float
    date: datetime

# Schema for creating crop data
class CropDataCreate(CropDataBase):
    pass

# Schema for reading crop data
class CropData(CropDataBase):
    id: int

    class Config:
        from_attributes = True  # Replaces orm_mode in Pydantic v2
