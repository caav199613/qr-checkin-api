from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
import enum

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

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo_identificacion = Column(Enum(TipoIdentificacion), nullable=False)
    numero_identificacion = Column(String(50), unique=True, nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    jornada = Column(Enum(Jornada), nullable=False)
    grado = Column(String(20), nullable=False)
    codigo_grado = Column(Integer,nullable=False)
    acudiente = Column(String(20),nullable=False)
    numero_acudiente = Column(String(20),nullable=False)
