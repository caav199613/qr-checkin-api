from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.models.admin import Usuario 

class UsuarioBase(BaseModel):
    Usuario: str
    contraseña: str
    

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    model_config = ConfigDict(from_attributes=True)

class UsuarioUpdate(BaseModel):
    Usuario: Optional[str] = None
    contrasela:Optional[str]=None
    
    model_config = ConfigDict(extra="forbid")
