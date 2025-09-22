from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.core.security import verify_password, hash_password
from app.models.conductor import Conductor
from app.schemas.conductor_schema import ConductorCreate, ConductorUpdate


def get_all(db: Session):
    """Obtener todos los conductores"""
    return db.query(Conductor).all()


def get_by_numero(db: Session, numero_id: str):
    """Buscar conductor por número de identificación"""
    return db.query(Conductor).filter(
        Conductor.numero_id == numero_id
    ).first()


def get_by_usuario(db: Session, usuario: str):
    """Buscar admin por número de identificación"""
    return db.query(Conductor).filter(
        Conductor.usuario == usuario
    ).first()


def create(db: Session, conductor_in: ConductorCreate):
    """Crear un nuevo conductor"""
    
    hashed_pw = hash_password(conductor_in.contrasena)  # 👈 generar hash

    conductor = Conductor(
        nombre=conductor_in.nombre,
        tipo_id=conductor_in.tipo_id,
        numero_id=conductor_in.numero_id,
        numero=conductor_in.numero,
        usuario=conductor_in.usuario,
        contrasena=hashed_pw,
    )

    db.add(conductor)
    try:
        db.commit()
        db.refresh(conductor)
        return conductor
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al crear el conductor.")

def update(db: Session, conductor_id: int, data: ConductorUpdate):
    conductor = get_by_numero(db, conductor_id)
    if not conductor:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")

    if data.nombre:
        data.nombre = to_capitalize(data.nombre.strip())

    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(conductor, k, v)

    try:
        db.commit()
        db.refresh(conductor)
        return conductor
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al actualizar el conductor.")

def delete(db: Session, conductor_id: int):
    """Eliminar un conductor"""
    conductor = get_by_numero(db, conductor_id)
    if not conductor:
        raise HTTPException(status_code=404, detail="Conductor no encontrado")

    db.delete(conductor)
    db.commit()
    return {"detail": "Conductor eliminado"}


def verify_credentials(db: Session, usuario: str, contrasena: str) -> bool:
    conductor = get_by_usuario(db, usuario)
    if not conductor:
        return False
    return verify_password(contrasena, conductor.contrasena)