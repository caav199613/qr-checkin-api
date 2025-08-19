from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional

# Base
class RegistroBase(BaseModel):
    id_estudiante: int
    id_bus: int
    fecha_y_hora: datetime

# Para crear
class RegistroCreate(RegistroBase):
    pass

# Para actualizar
class RegistroUpdate(BaseModel):
    id_estudiante: Optional[int] = None
    id_bus: Optional[int] = None
    fecha_y_hora: Optional[datetime] = None

# Para respuesta
class RegistroResponse(RegistroBase):
    registro: int  # identificador único (PK)
    model_config = ConfigDict(from_attributes=True)
