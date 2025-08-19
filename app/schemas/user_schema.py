from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.models.user import TipoIdentificacion, Jornada  # 👈 Importa Jornada ya corregida

class UsuarioBase(BaseModel):
    nombre: str
    tipo_identificacion: TipoIdentificacion
    numero_identificacion: str
    correo: EmailStr
    telefono: Optional[str] = None
    jornada: Jornada        # 👈 Ahora sí correcto
    grado: str
    codigo_grado: int
    acudiente: str
    numero_acudiente: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    model_config = ConfigDict(from_attributes=True)

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo_identificacion: Optional[TipoIdentificacion] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    jornada: Optional[Jornada] = None   # 👈 Aquí también
    grado: Optional[str] = None
    codigo_grado: Optional[int] = None  # 👈 también lo corregí a int
    acudiente: Optional[str] = None
    numero_acudiente: Optional[str] = None

    model_config = ConfigDict(extra="forbid")
