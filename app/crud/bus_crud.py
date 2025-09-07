from sqlalchemy.orm import Session
from app.models.bus import Bus
from app.schemas.bus_schema import BusCreate, BusUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def get_all(db: Session):
    """Obtener todos los buses"""
    return db.query(Bus).all()


def get_by_placa(db: Session, placa: str):
    """Buscar un bus por placa"""
    return db.query(Bus).filter(Bus.placa == placa).first()


def create(db: Session, bus_in: BusCreate):
    """Crear un bus nuevo"""
    # Validar duplicados en placa
    if get_by_placa(db, bus_in.placa):
        raise HTTPException(status_code=409, detail="La placa ya está registrada.")

    # Crear instancia
    bus = Bus(**bus_in.model_dump())
    db.add(bus)

    try:
        db.commit()
        db.refresh(bus)
        return bus
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad: placa o empresa duplicada.")


def update(db: Session, placa: int, data: BusUpdate):
    """Actualizar un bus por placa"""
    bus = get_by_placa(db, placa)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus no encontrado")

    # Validar si se intenta cambiar placa y ya existe en otro bus
    if data.placa and data.placa != bus.placa and get_by_placa(db, data.placa):
        raise HTTPException(status_code=409, detail="La placa ya está registrada.")

    # Actualizar solo los campos enviados
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(bus, k, v)

    try:
        db.commit()
        db.refresh(bus)
        return bus
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al actualizar el bus.")


def delete(db: Session, placa: int):
    """Eliminar un bus por placa"""
    bus = get_by_placa(db, placa)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus no encontrado")

    db.delete(bus)
    db.commit()
    return {"detail": "Bus eliminado"}
