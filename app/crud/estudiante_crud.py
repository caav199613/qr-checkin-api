from sqlalchemy.orm import Session
from app.models.estudiante import estudiante
from app.schemas.estudiante_schema import estudianteCreate, estudianteUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def get_all(db: Session):
    """Obtener todos los estudiantes"""
    return db.query(estudiante).all()
6

def get_by_numero(db: Session, numero_identificacion: str):
    """Buscar estudiante por número de identificación"""
    return db.query(estudiante).filter(
        estudiante.numero_identificacion == numero_identificacion
    ).first()


def get_by_correo(db: Session, correo: str):
    """Buscar estudiante por correo"""
    return db.query(estudiante).filter(estudiante.correo == correo).first()


def create(db: Session, estudiante_in: estudianteCreate):
    """Crear un estudiante nuevo"""
    # Validar duplicados
    if get_by_numero(db, estudiante_in.numero_identificacion):
        raise HTTPException(status_code=409, detail="El número de identificación ya está registrado.")

    if get_by_correo(db, estudiante_in.correo):
        raise HTTPException(status_code=409, detail="El correo ya está registrado.")
    
    # Crear instancia
    estudiante = estudiante(**estudiante_in.model_dump())  # Pydantic v2
    db.add(estudiante)

    try:
        db.commit()
        db.refresh(estudiante)
        return estudiante
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad: número de identificación o correo duplicado.")


def update_by_numero(db: Session, numero_path: str, data: estudianteUpdate):
    """Actualizar estudiante por número de identificación"""
    estudiante = db.query(estudiante).filter(estudiante.numero_identificacion == numero_path).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="estudiante no encontrado")

    # 🚫 No permitir cambiar el número de identificación
    if "numero_identificacion" in data.model_dump(exclude_unset=True):
        raise HTTPException(status_code=400, detail="No se permite cambiar el número de identificación")

    # ✅ Validar correo solo si lo cambió
    if data.correo and data.correo != estudiante.correo:
        if get_by_correo(db, data.correo):
            raise HTTPException(status_code=409, detail="El correo ya está registrado.")

    # ✅ Actualizar solo los campos enviados
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(estudiante, k, v)

    try:
        db.commit()
        db.refresh(estudiante)
        return estudiante
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al actualizar el estudiante.")


def delete_by_numero(db: Session, numero_identificacion: str):
    """Eliminar estudiante por número de identificación"""
    estudiante = get_by_numero(db, numero_identificacion)
    if not estudiante:
        raise HTTPException(status_code=404, detail="estudiante no encontrado")

    db.delete(estudiante)
    db.commit()
    return {"detail": "estudiante eliminado"}
