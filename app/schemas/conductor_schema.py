from pydantic import BaseModel
from typing import Optional

class ConductorBase(BaseModel):
    nombre_conductor: str
    numero_id: str
    tipo_id: str
    numero_conductor: str

class ConductorCreate(ConductorBase):
    pass

class ConductorUpdate(BaseModel):
    nombre_conductor: Optional[str] = None
    numero_id: Optional[str] = None
    tipo_id: Optional[str] = None
    numero_conductor: Optional[str] = None

    class Config:
        extra = "forbid"  # para no aceptar campos extra

class ConductorResponse(ConductorBase):
    id: int

    class Config:
        from_attributes = True  # antes orm_mode = True
