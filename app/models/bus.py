from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship
import uuid

class Bus(Base):
    __tablename__ = "bus"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    placa = Column(String(10),unique=True, nullable=False)
    empresa = Column(String(50), nullable=False)
    numero = Column(String(10), nullable=False)


    registros = relationship("RegistroRuta", back_populates="bus")