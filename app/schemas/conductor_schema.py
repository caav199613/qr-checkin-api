from pydantic import BaseModel
from typing import Optional

class ConductorBase(BaseModel):
    nombre: str
    numero_id: str
    tipo_id: str
    numero: str
    usuario: str
class ConductorCreate(ConductorBase):
    contraseña: str

class ConductorUpdate(BaseModel):
    nombre: Optional[str] = None
    numero_id: Optional[str] = None
    tipo_id: Optional[str] = None
    numero: Optional[str] = None
    contraseña: Optional[str] = None
    
    class Config:
        extra = "forbid"  # para no aceptar campos extra

class ConductorResponse(ConductorBase):
    id: str

    class Config:
        from_attributes = True  # antes orm_mode = True


class ConductorLogin(BaseModel):
    usuario: str
    contrasena: str   # texto plano para comprobar