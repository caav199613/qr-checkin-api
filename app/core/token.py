
import jwt
from datetime import datetime, timedelta

SECRET = "qr_checking"
ALGO = "HS256"

def crear_token(usuario: str) -> str:
    payload = {
        "sub": usuario,
        "exp": datetime.utcnow() + timedelta(hours=2),
        "iat": datetime.utcnow(),
    }
    return jwt.encode(payload, SECRET, algorithm=ALGO)
