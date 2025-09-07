from sqlalchemy import Column,String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid
import enum

class RegistroRuta(Base):
    __tablename__ = "registros_ruta"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # este es el "registro"
    id_estudiante = Column(String(36), ForeignKey("estudiante.id"), nullable=False)
    id_bus = Column(String(36), ForeignKey("bus.id"), nullable=False)
    id_conductor = Column(String(36), ForeignKey("conductor.id"),nullable=False)
    fecha_y_hora = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="registros")
    bus = relationship("Bus", back_populates="registros")
    conductor = relationship("Conductor", back_populates="registros") 