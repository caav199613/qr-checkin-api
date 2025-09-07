import bcrypt
from models.admin import Admin

# Crear hash
hashed = bcrypt.hashpw("mi_contraseña".encode("utf-8"), bcrypt.gensalt())

# Guardar en DB
admin = Admin(usuario="admin1", contrasena=hashed)

# Verificar
bcrypt.checkpw("mi_contraseña".encode("utf-8"), admin.contrasena)  # True o False
