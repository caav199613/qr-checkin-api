from pydantic import BaseModel, ConfigDict
from typing import Optional

# Base
class BusBase(BaseModel):
    placa : str
    empresa: str 
    numero: str

# Para crear
class BusCreate(BusBase):
    pass

# Para actualizar
class BusUpdate(BaseModel):
    placa : Optional[str] = None
    empresa : Optional[str] = None
    numero : Optional[str] = None

# Para respuesta
class BusResponse(BusBase):
    id: str  # identificador único (PK)
    model_config = ConfigDict(from_attributes=True)
