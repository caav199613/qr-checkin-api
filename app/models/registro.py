from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class RegistroRuta(Base):
    __tablename__ = "registros_ruta"

    id = Column(Integer, primary_key=True, index=True)  # este es el "registro"
    id_estudiante = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    id_bus = Column(Integer, ForeignKey("bus.id"), nullable=False)
    id_conductor = Column(Integer, ForeignKey("conductor.id"),nullable=False)
    fecha_y_hora = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="registros")
    bus = relationship("Bus", back_populates="registros")
    conductor = relationship("conductor", back_populates="registros") 