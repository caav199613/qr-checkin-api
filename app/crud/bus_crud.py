from sqlalchemy.orm import Session
from app.models.bus import Bus
from app.schemas.bus_schema import BusCreate, BusUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def get_all(db: Session):
    """Obtener todos los buses"""
    return db.query(Bus).all()


def get_by_id(db: Session, bus_id: int):
    """Buscar un bus por ID"""
    return db.query(Bus).filter(Bus.id == bus_id).first()


def get_by_placa(db: Session, placa: str):
    """Buscar un bus por placa"""
    return db.query(Bus).filter(Bus.placa == placa).first()


def create(db: Session, bus_in: BusCreate):
    """Crear un bus nuevo"""
    # Validar duplicados en placa y empresa
    if get_by_placa(db, bus_in.placa):
        raise HTTPException(status_code=409, detail="La placa ya está registrada.")

    if db.query(Bus).filter(Bus.empresa == bus_in.empresa).first():
        raise HTTPException(status_code=409, detail="La empresa ya tiene un bus registrado.")

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


def update(db: Session, bus_id: int, data: BusUpdate):
    """Actualizar un bus por ID"""
    bus = get_by_id(db, bus_id)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus no encontrado")

    # Validar si se intenta cambiar placa y ya existe en otro bus
    if data.placa and data.placa != bus.placa:
        if get_by_placa(db, data.placa):
            raise HTTPException(status_code=409, detail="La placa ya está registrada.")

    # Validar si se intenta cambiar empresa y ya existe en otro bus
    if data.empresa and data.empresa != bus.empresa:
        if db.query(Bus).filter(Bus.empresa == data.empresa).first():
            raise HTTPException(status_code=409, detail="La empresa ya tiene un bus registrado.")

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


def delete(db: Session, bus_id: int):
    """Eliminar un bus por ID"""
    bus = get_by_id(db, bus_id)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus no encontrado")

    db.delete(bus)
    db.commit()
    return {"detail": "Bus eliminado"}
