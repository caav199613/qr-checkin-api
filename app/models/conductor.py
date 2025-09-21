from sqlalchemy import Column, Enum,LargeBinary, String
from app.core.database import Base
from sqlalchemy.orm import relationship
import uuid
import enum

class TipoIdentificacion(str, enum.Enum):
    CC = "CC"
    CE = "CE"
    Pasaporte = "Pasaporte"

class Conductor(Base):
    __tablename__ = "conductor"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(100),nullable=False)
    tipo_id = Column(Enum(TipoIdentificacion), nullable=False)
    numero_id = Column(String(20), unique=True, nullable=False)
    numero = Column(String (15), nullable=False)
    usuario = Column(String (20), unique=True, nullable=False)
    contrasena = Column(LargeBinary, nullable=False)  # almacena el hash en binario

    registros = relationship("RegistroRuta", back_populates="conductor")