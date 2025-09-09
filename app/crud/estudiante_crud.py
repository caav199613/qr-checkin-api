from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models.estudiante import Estudiante
from app.schemas.estudiante_schema import EstudianteCreate, EstudianteUpdate


def get_all(db: Session):
    """Obtener todos los estudiantes."""
    return db.query(Estudiante).all()


def get_by_numero(db: Session, numero_identificacion: str):
    """Buscar estudiante por número de identificación."""
    return (
        db.query(Estudiante)
        .filter(Estudiante.numero_identificacion == numero_identificacion)
        .first()
    )


def get_by_correo(db: Session, correo: str):
    """Buscar estudiante por correo."""
    return db.query(Estudiante).filter(Estudiante.correo == correo).first()


def create(db: Session, estudiante_in: EstudianteCreate):
    """Crear un estudiante nuevo (valida duplicados de número y correo)."""
    if get_by_numero(db, estudiante_in.numero_identificacion):
        raise HTTPException(status_code=409, detail="El número de identificación ya está registrado.")

    if get_by_correo(db, estudiante_in.correo):
        raise HTTPException(status_code=409, detail="El correo ya está registrado.")

    estudiante = Estudiante(**estudiante_in.model_dump())  # Pydantic v2
    db.add(estudiante)

    try:
        db.commit()
        db.refresh(estudiante)
        return estudiante
    except IntegrityError:
        db.rollback()
        # Respaldo por si la BD lanza la violación de UNIQUE
        raise HTTPException(status_code=409, detail="Error de integridad: número de identificación o correo duplicado.")


def update_by_numero(db: Session, numero_path: str, data: EstudianteUpdate):
    """
    Actualizar estudiante por número de identificación (path).
    - Permite cambiar numero_identificacion SOLO si no existe en otro estudiante.
    - Valida duplicado de correo si cambia.
    - Actualiza solo campos enviados.
    """
    estudiante = (
        db.query(Estudiante)
        .filter(Estudiante.numero_identificacion == numero_path)
        .first()
    )
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado.")

    cambios = data.model_dump(exclude_unset=True)

    # Validar cambio de numero_identificacion (si viene y es distinto)
    nuevo_num = cambios.get("numero_identificacion")
    if nuevo_num and nuevo_num != estudiante.numero_identificacion:
        existente = (
            db.query(Estudiante)
            .filter(Estudiante.numero_identificacion == nuevo_num)
            .first()
        )
        if existente and existente.id != estudiante.id:
            raise HTTPException(status_code=409, detail="El número de identificación ya está registrado.")
        # Aplicar el cambio si pasó la validación
        estudiante.numero_identificacion = nuevo_num

    # Validar cambio de correo (si viene y es distinto)
    nuevo_correo = cambios.get("correo")
    if nuevo_correo and nuevo_correo != estudiante.correo:
        if get_by_correo(db, nuevo_correo):
            raise HTTPException(status_code=409, detail="El correo ya está registrado.")
        estudiante.correo = nuevo_correo

    # Actualizar resto de campos enviados (excepto los que ya manejamos arriba)
    for k, v in cambios.items():
        if k in {"numero_identificacion", "correo"}:
            continue
        setattr(estudiante, k, v)

    try:
        db.commit()
        db.refresh(estudiante)
        return estudiante
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Error de integridad al actualizar el estudiante.")


def delete_by_numero(db: Session, numero_identificacion: str):
    """Eliminar estudiante por número de identificación."""
    estudiante = get_by_numero(db, numero_identificacion)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado.")

    db.delete(estudiante)
    db.commit()
    return {"detail": "Estudiante eliminado."}
