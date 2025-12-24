from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud, database
from database import engine, SessionLocal
import requests, os
from dotenv import load_dotenv

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to FarmIQ Backend 🚜"}

@app.get("/nasa-data")
def get_nasa_data():
    api_key = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    r = requests.get(url)
    return r.json()

@app.post("/crop-data/")
def create_crop(crop: schemas.CropDataCreate, db: Session = Depends(get_db)):
    return crud.create_crop_data(db, crop)

@app.get("/crop-data/")
def read_crops(db: Session = Depends(get_db)):
    return crud.get_all_crop_data(db)
