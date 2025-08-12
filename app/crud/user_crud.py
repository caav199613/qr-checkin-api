from sqlalchemy.orm import Session
from app.models.user import Usuario
from app.schemas.user_schema import UsuarioCreate, UsuarioUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def get_all(db: Session):
    return db.query(Usuario).all()

def get_by_numero(db: Session, numero_identificacion: str):
    return db.query(Usuario).filter(
        Usuario.numero_identificacion == numero_identificacion
    ).first()

def get_by_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()


def create(db: Session, usuario_in: UsuarioCreate):
    existe = get_by_numero(db, usuario_in.numero_identificacion)
    if existe:
        raise HTTPException(status_code=409, detail="El número de identificación ya está registrado.")

    if get_by_correo(db, usuario_in.correo):
        raise HTTPException(status_code=409, detail="El correo ya está registrado.")
    
    user = Usuario(**usuario_in.model_dump())  # Pydantic v2
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        # por si ocurre race condition
        raise HTTPException(status_code=409, detail="El número de identificación ya está registrado.")

def update_by_numero(db: Session, numero_path: str, data: UsuarioUpdate):
    user = db.query(Usuario).filter(Usuario.numero_identificacion == numero_path).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Si el cliente envía numero_identificacion en el body, lo rechazamos
    if hasattr(data, "numero_identificacion"):
        raise HTTPException(status_code=400, detail="No se permite cambiar el número de identificación")

    if get_by_correo(db, data.correo):
        raise HTTPException(status_code=409, detail="El correo ya está registrado.")
    
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(user, k, v)

    db.commit()
    db.refresh(user)
    return user

def delete_by_numero(db: Session, numero_identificacion: str):
    user = get_by_numero(db, numero_identificacion)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"detail": "Usuario eliminado"}