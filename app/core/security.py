# app/utils/security.py
import bcrypt

def hash_password(plain_password: str) -> bytes:
    """
    Genera un hash (bytes) con bcrypt a partir de una contraseña en texto plano.
    """
    if not isinstance(plain_password, str) or not plain_password:
        raise ValueError("La contraseña debe ser un string no vacío.")
    return bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())

def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    """
    Verifica si 'plain_password' coincide con 'hashed_password' (bcrypt).
    """
    if not isinstance(hashed_password, (bytes, bytearray)):
        raise TypeError("hashed_password debe ser bytes/bytearray (LargeBinary en la BD).")
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)

def decrypt_password(_hashed_password: bytes) -> str:
    """
    NO ES POSIBLE. Los hashes bcrypt son unidireccionales.
    Se incluye solo para claridad: siempre lanzará un error.
    """
    raise NotImplementedError(
        "Las contraseñas no se pueden 'desencriptar'. "
        "Use verify_password(plain, hashed) para comprobarlas."
    )