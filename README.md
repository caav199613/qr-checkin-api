# qr-checkin-api
Este proyecto es un sistema backend desarrollado para gestionar el registro y control de pasajeros mediante códigos QR. Proporciona una API RESTful segura que permite a los usuarios escanear un QR personalizado para validar su identidad, registrar su entrada o salida, y almacenar su información de viaje en una base de datos centralizada.


## Requisitos previos
Tener Python 3.8+ instalado
Tener MySQL instalado y corriendo
Tener acceso a consola o terminal (CMD, PowerShell, Bash)

* Crear archivo .env:

Se debe duplicar el archivo .env.test y se renombra .env

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

* Crear archivo .env con las credenciales de acceso a la base de datos MySQL


* Crear base de datos MySQL

```cmd
python -m app.create_db
```

* Correr la Aplicacion

```cmd
uvicorn app.main:app --reload
```


## Abrir el navegador y probar
En el navegador abre:
Interfaz grafica de documetacion que ofrece el framework "Fast API"
```arduino
http://127.0.0.1:8000/docs
```
