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

```
uvicorn app.main:app --reload
```


## Abrir el navegador y probar
En el navegador abre:
Interfaz grafica de documetacion que ofrece el framework "Fast API"
```arduino
http://127.0.0.1:8000/docs
```


## Crear Qrs para la aplicacion android

* una ves creados los estudiantes en la base de datos, hacemos una solicitud GET a
```arduino
http://127.0.0.1:8000/estudiantes
```

con esto obtenemos la lista de estudiantes similar a esto 
```arduino
[
    {
        "nombre": "sa",
        "tipo_identificacion": "TI",
        "numero_identificacion": "12",
        "correo": "string@example.com",
        "telefono": "1",
        "jornada": "mañana",
        "grado": "string",
        "codigo_grado": 0,
        "acudiente": "string",
        "numero_acudiente": "string"
    },
    {
        "nombre": "carlos",
        "tipo_identificacion": "TI",
        "numero_identificacion": "123",
        "correo": "string1@example.com",
        "telefono": "123",
        "jornada": "mañana",
        "grado": "11",
        "codigo_grado": 2,
        "acudiente": "juan",
        "numero_acudiente": "12"
    }
]
```
copiamos el texto a nuesto archivo ubicado en datos.txt reemplazando cualquier texto que existiera en este archivo y limpiamos la carpeta en generador_qr/qrs, eliminando todas las imagenes que pueda contener.

y ejecutamos el siguiente comando desde la raiz de la aplicacion

```arduino
python generador_qr/generar_qrs.py 
```
