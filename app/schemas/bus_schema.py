from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from app.core.config import to_upper


 
class BusBase(BaseModel):
    placa : str
    empresa: str 
    numero: str

    @field_validator("placa")
    def normalize_placa(cls, v: str) -> str:
        return to_upper(v.strip()) if v else v
# Para crear
class BusCreate(BusBase):
    pass

# Para actualizar
class BusUpdate(BaseModel):
    placa : Optional[str] = None
    empresa : Optional[str] = None
    numero : Optional[str] = None


    @field_validator("placa")
    def normalize_placa(cls, v: Optional[str]) -> Optional[str]:
        return to_upper(v.strip()) if v else v
    
# Para respuesta
class BusResponse(BusBase):
    id: str  # identificador único (PK)
    model_config = ConfigDict(from_attributes=True)
