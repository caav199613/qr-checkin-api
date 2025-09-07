from sqlalchemy import Column, Integer, String,LargeBinary
from app.core.database import Base
import uuid
import enum

class Admin(Base):
    __tablename__ = "admin"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    usuario = Column(String(50), unique=True, nullable=False)
    contrasena = Column(LargeBinary, nullable=False)  # almacena el hash en binario
