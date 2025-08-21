from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base


class Usuario(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    Usuario = Column(String(100), unique=True, nullable=False)
    contraseña= Column( String(100), nullable=False)