from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.user import TipoIdentificacion

class UsuarioBase(BaseModel):
    nombre: str
    tipo_identificacion: TipoIdentificacion
    numero_identificacion: str
    correo: EmailStr
    telefono: Optional[str]

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
