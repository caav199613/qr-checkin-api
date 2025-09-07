from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
import enum
import uuid
class TipoIdentificacion(str, enum.Enum):
    CC = "CC"
    CE = "CE"
    TI = "TI"
    RC = "RC"
    Pasaporte = "Pasaporte"

class Jornada(str, enum.Enum):   
    tarde = "tarde"
    unica = "unica"
    manana= "manana"

class Estudiante(Base):
    __tablename__ = "estudiante"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(100), nullable=False)
    tipo_identificacion = Column(Enum(TipoIdentificacion), nullable=False)
    numero_identificacion = Column(String(50), unique=True, nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    jornada = Column(Enum(Jornada), nullable=False)
    grado = Column(String(20), nullable=False)
    codigo_grado = Column(Integer,nullable=False)
    acudiente = Column(String(50),nullable=False)
    numero_acudiente = Column(String(20),nullable=False)
