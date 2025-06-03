# qr-checkin-api
Este proyecto es un sistema backend desarrollado para gestionar el registro y control de pasajeros mediante códigos QR. Proporciona una API RESTful segura que permite a los usuarios escanear un QR personalizado para validar su identidad, registrar su entrada o salida, y almacenar su información de viaje en una base de datos centralizada.


## Requisitos previos
Tener Python 3.8+ instalado
Tener MySQL instalado y corriendo
Tener acceso a consola o terminal (CMD, PowerShell, Bash)


* Crear entorno virtual

```cmd
py -m venv venv
```

* Activar entorno virtual:

```cmd
venv\Scripts\activate
```

* Instalar depedencias:

```
pip install -r requirements.txt
```

* Crear base de datos MySQL

```sql
CREATE DATABASE usuariosdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```


