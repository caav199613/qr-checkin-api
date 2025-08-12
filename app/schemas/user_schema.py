# app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.models.user import TipoIdentificacion  # Enum que usas en el modelo

class UsuarioBase(BaseModel):
    nombre: str
    tipo_identificacion: TipoIdentificacion
    numero_identificacion: str
    correo: EmailStr
    telefono: Optional[str] = None  # default None para que sea opcional

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    # Si ya no devuelves id, no necesitas nada extra aquí
    model_config = ConfigDict(from_attributes=True)  # reemplaza orm_mode

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo_identificacion: Optional[TipoIdentificacion] = None  # si no quieres que cambie, quítalo
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None

    model_config = ConfigDict(extra="forbid")  # rechaza campos no definidos