from pydantic import BaseModel, field_validator
from typing import Optional
from app.core.config import to_capitalize
from app.models.conductor import TipoIdentificacion  # 👈 usamos la misma función


class EstudianteBase(BaseModel):
    nombre: str
    tipo_identificacion: TipoIdentificacion
    numero_identificacion: str
    correo: str
    telefono: str
    jornada: str
    grado: str
    codigo_grado: int
    acudiente: str
    numero_acudiente: str

    # 👇 Normalizamos el nombre al guardar
    @field_validator("nombre", "acudiente")
    def normalize_fields(cls, v: str) -> str:
        return to_capitalize(v.strip()) if v else v


class EstudianteCreate(EstudianteBase):
    pass


class EstudianteUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo_identificacion: Optional[TipoIdentificacion] = None
    numero_identificacion: Optional[str] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None
    jornada: Optional[str] = None
    grado: Optional[str] = None
    codigo_grado: Optional[int] = None
    acudiente: Optional[str] = None
    numero_acudiente: Optional[str] = None

    @field_validator("nombre", "acudiente")
    def normalize_fields(cls, v: Optional[str]) -> Optional[str]:
        return to_capitalize(v.strip()) if v else v

    class Config:
        extra = "forbid"


class EstudianteResponse(EstudianteBase):
    id: str

    class Config:
        from_attributes = True
