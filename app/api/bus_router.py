from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.bus_schema import BusCreate, BusUpdate, BusResponse
from app.crud import bus_crud   # 👈 tu crud de buses
from app.dependencies.db import get_db

router = APIRouter(
    prefix="/buses",
    tags=["Buses"]
)


@router.get("/", response_model=List[BusResponse])
def listar_buses(db: Session = Depends(get_db)):
    """Obtener todos los buses"""
    return bus_crud.get_all(db)


@router.get("/{bus_id}", response_model=BusResponse)
def obtener_bus(bus_id: int, db: Session = Depends(get_db)):
    """Obtener un bus por ID"""
    bus = bus_crud.get_by_id(db, bus_id)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus no encontrado")
    return bus


@router.post("/", response_model=BusResponse, status_code=201)
def crear_bus(bus_in: BusCreate, db: Session = Depends(get_db)):
    """Crear un nuevo bus"""
    return bus_crud.create(db, bus_in)


@router.put("/{bus_id}", response_model=BusResponse)
def actualizar_bus(bus_id: int, bus_in: BusUpdate, db: Session = Depends(get_db)):
    """Actualizar un bus por ID"""
    return bus_crud.update(db, bus_id, bus_in)


@router.delete("/{bus_id}")
def eliminar_bus(bus_id: int, db: Session = Depends(get_db)):
    """Eliminar un bus por ID"""
    return bus_crud.delete(db, bus_id)
