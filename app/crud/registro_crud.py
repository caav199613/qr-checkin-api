from sqlalchemy.orm import Session
from app.models.registro import RegistroRuta   # 👈 ajusta la ruta según tu proyecto
from app.schemas.registro_schema import RegistroCreate, RegistroUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def get_all(db: Session):
    """Obtener todos los registros de ruta"""
    return db.query(RegistroRuta).all()


def get_by_id(db: Session, registro_id: int):
    """Buscar un registro de ruta por ID"""
    return db.query(RegistroRuta).filter(RegistroRuta.id == registro_id).first()


def create(db: Session, registro_in: RegistroCreate):
    """Crear un nuevo registro de ruta"""
    registro = RegistroRuta(**registro_in.model_dump())
    db.add(registro)

    try:
        db.commit()
        db.refresh(registro)
        return registro
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al crear el registro.")


def update(db: Session, registro_id: int, data: RegistroUpdate):
    """Actualizar un registro de ruta por ID"""
    registro = get_by_id(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    # Actualizar solo los campos enviados
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(registro, k, v)

    try:
        db.commit()
        db.refresh(registro)
        return registro
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al actualizar el registro.")


def delete(db: Session, registro_id: int):
    """Eliminar un registro de ruta por ID"""
    registro = get_by_id(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    db.delete(registro)
    db.commit()
    return {"detail": "Registro eliminado"}
