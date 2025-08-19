from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Conductor(Base):
    __tablename__ = "conductor"

    id = Column(Integer, primary_key=True, index=True)
    nombre_conductor = Column(String(100),nullable=False)
    numero_id = Column(String(20),nullable=False)
    tipo_id = Column(String(20),nullable=False)
    numero_conductor = Column(String(20),nullable=False)