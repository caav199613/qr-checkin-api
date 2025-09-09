from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.models.estudiante import TipoIdentificacion, Jornada  

class EstudianteBase(BaseModel):
    nombre: str
    tipo_identificacion: TipoIdentificacion
    numero_identificacion: str
    correo: EmailStr
    telefono: Optional[str] = None
    jornada: Jornada 
    grado: str
    codigo_grado: int
    acudiente: str
    numero_acudiente: str

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteResponse(EstudianteBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class EstudianteUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo_identificacion: Optional[TipoIdentificacion] = None
    numero_identificacion: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    jornada: Optional[Jornada] = None   # 👈 Aquí también
    grado: Optional[str] = None
    codigo_grado: Optional[int] = None  # 👈 también lo corregí a int
    acudiente: Optional[str] = None
    numero_acudiente: Optional[str] = None

    model_config = ConfigDict(extra="forbid")
