from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models.conductor import Conductor
from app.schemas.conductor_schema import ConductorCreate, ConductorUpdate


def get_all(db: Session):
    """Obtener todos los conductores"""
    return db.query(Conductor).all()


def get_by_id(db: Session, conductor_id: int):
    """Buscar un conductor por ID"""
    return db.query(Conductor).filter(Conductor.id == conductor_id).first()


def create(db: Session, conductor_in: ConductorCreate):
    """Crear un nuevo conductor"""
    conductor = Conductor(**conductor_in.model_dump())
    db.add(conductor)
    try:
        db.commit()
        db.refresh(conductor)
        return conductor
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al crear el conductor.")


def update(db: Session, conductor_id: int, data: ConductorUpdate):
    """Actualizar un conductor"""
    conductor = get_by_id(db, conductor_id)
    if not conductor:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")

    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(conductor, k, v)

    try:
        db.commit()
        db.refresh(conductor)
        return conductor
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al actualizar el conductor.")


def delete(db: Session, conductor_id: int):
    """Eliminar un conductor"""
    conductor = get_by_id(db, conductor_id)
    if not conductor:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")

    db.delete(conductor)
    db.commit()
    return {"detail": "Conductor eliminado"}

