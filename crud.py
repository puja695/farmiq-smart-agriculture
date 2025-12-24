from sqlalchemy.orm import Session
import models, schemas

def create_crop_data(db: Session, crop: schemas.CropDataCreate):
    db_crop = models.CropData(**crop.dict())
    db.add(db_crop)
    db.commit()
    db.refresh(db_crop)
    return db_crop

def get_all_crop_data(db: Session):
    return db.query(models.CropData).all()
