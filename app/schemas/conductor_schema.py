from pydantic import BaseModel, field_validator
from typing import Optional
from app.models.conductor import TipoIdentificacion
from app.core.config import to_capitalize  # 👈 usamos la función unificada


class ConductorBase(BaseModel):
    nombre: str
    numero_id: str
    tipo_id: TipoIdentificacion
    numero: str
    usuario: str

    @field_validator("nombre")
    def normalize_nombre(cls, v: str) -> str:
        return to_capitalize(v.strip()) if v else v


class ConductorCreate(ConductorBase):
    contrasena: str


class ConductorUpdate(BaseModel):
    nombre: Optional[str] = None
    numero_id: Optional[str] = None
    tipo_id: Optional[TipoIdentificacion] = None
    numero: Optional[str] = None
    contrasena: Optional[str] = None

    @field_validator("nombre")
    def normalize_nombre(cls, v: Optional[str]) -> Optional[str]:
        return to_capitalize(v.strip()) if v else v

    class Config:
        extra = "forbid"  # para no aceptar campos extra


class ConductorResponse(ConductorBase):
    id: str

    class Config:
        from_attributes = True  # antes orm_mode = True


class ConductorLogin(BaseModel):
    usuario: str
    contrasena: str  # texto plano para comprobar
