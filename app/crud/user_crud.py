from sqlalchemy.orm import Session
from app.models.user import Usuario
from app.schemas.user_schema import UsuarioCreate

def get_all(db: Session):
    return db.query(Usuario).all()

def get_by_id(db: Session, user_id: int):
    return db.query(Usuario).filter(Usuario.id == user_id).first()

def create(db: Session, user: UsuarioCreate):
    db_user = Usuario(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update(db: Session, user_id: int, user_data: UsuarioCreate):
    user = get_by_id(db, user_id)
    if user:
        for key, value in user_data.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user

def delete(db: Session, user_id: int):
    user = get_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user
