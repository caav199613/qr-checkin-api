from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Bus(Base):
    __tablename__ = "bus"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10),unique=True, nullable=False)
    empresa = Column(String(100),unique=True, nullable=False)
    numero = Column(String(10), nullable=False)
