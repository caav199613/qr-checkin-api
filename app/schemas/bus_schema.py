from pydantic import BaseModel, ConfigDict
from typing import Optional

# Base
class BusBase(BaseModel):
    placa : int
    empresa: str 
    numero: str

# Para crear
class BusCreate(BusBase):
    pass

# Para actualizar
class BusUpdate(BaseModel):
    placa : Optional[int] = None
    empresa : Optional[str] = None
    numero : Optional[str] = None

# Para respuesta
class BusResponse(BusBase):
    registro: int  # identificador único (PK)
    model_config = ConfigDict(from_attributes=True)
