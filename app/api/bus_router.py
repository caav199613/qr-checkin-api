from app.core.config import to_upper

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


@router.get("/{placa}", response_model=BusResponse)
def obtener_bus_por_placa(placa: str, db: Session = Depends(get_db)):
    """Obtener un bus por su número de placa"""
    bus = bus_crud.get_by_placa(db, placa)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus no encontrado")
    return bus

@router.post("/", response_model=BusResponse, status_code=201)
def crear_bus(bus_in: BusCreate, db: Session = Depends(get_db)):
    """Crear un nuevo bus"""
    return bus_crud.create(db, bus_in)


@router.put("/{placa}", response_model=BusResponse)
def actualizar_bus(placa: int, bus_in: BusUpdate, db: Session = Depends(get_db)):
    
    return bus_crud.update(db, placa, bus_in)


@router.delete("/{placa}")
def eliminar_bus(placa: int, db: Session = Depends(get_db)):
    """Eliminar un bus por placa"""
    return bus_crud.delete(db, placa)
