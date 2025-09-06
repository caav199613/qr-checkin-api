from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Conductor(Base):
    __tablename__ = "conductor"

    id = Column(Integer, primary_key=True, index=True)
    nombre_conductor = Column(String(100),nullable=False)
    numero_id = Column(String(20), unique=True, nullable=False)
    usuario_conductor = Column(String (String), unique=True, nullable=False)
    contraseña_conductor = Column(String (String), nullable=False)
    