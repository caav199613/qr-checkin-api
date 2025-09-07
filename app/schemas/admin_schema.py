from pydantic import BaseModel, ConfigDict


# Base: lo que comparten todos
class AdminBase(BaseModel):
    usuario: str


# Para crear -> requiere contraseña como texto plano (se hasheará antes de guardar)
class AdminCreate(AdminBase):
    contrasena: str


class AdminResponse(AdminBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class AdminUpdate(BaseModel):
    contrasena: str

    model_config = ConfigDict(extra="forbid")
