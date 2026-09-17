# RRHH Django API

Backend REST para la gestión de empleados, desarrollado con **Django** y **Django REST Framework**, conectado a **MySQL**. Expone un CRUD completo consumido por un frontend en [React](https://github.com/brianmatiasllampa/RRHH-REACT).

## Tecnologías

- Python 3
- Django 6
- Django REST Framework
- django-cors-headers
- MySQL (PyMySQL)
- python-dotenv

## Requisitos previos

- Python 3.10+
- MySQL corriendo localmente (o accesible por red)
- Una base de datos creada para el proyecto

## Instalación

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/brianmatiasllampa/rrhh-django-api.git
   cd rrhh-django-api
   ```

2. Creá y activá un entorno virtual:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\Activate.ps1
   # Mac/Linux
   source .venv/bin/activate
   ```

3. Instalá las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Copiá el archivo de variables de entorno de ejemplo y completá tus datos:
   ```bash
   cp rh_django/.env.example rh_django/.env
   ```
   Editá `rh_django/.env`:
   ```
   DJANGO_SECRET_KEY=generá-una-clave-secreta-propia
   DB_NAME=nombre_de_tu_base
   DB_USER=usuario
   DB_PASSWORD=contraseña
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

5. Aplicá las migraciones:
   ```bash
   cd rh_django
   python manage.py migrate
   ```

## Uso

```bash
python manage.py runserver
```

El servidor levanta por defecto en `http://127.0.0.1:8000`.

## Endpoints principales

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/empleados` | Lista todos los empleados |
| POST | `/api/empleados` | Crea un nuevo empleado |
| GET | `/api/empleados/<id>` | Detalle de un empleado |
| PUT | `/api/empleados/<id>` | Edita un empleado existente |
| DELETE | `/api/empleados/<id>` | Elimina un empleado |

## CORS

El backend acepta peticiones desde `http://localhost:4200` (Angular) y `http://localhost:5173` (React/Vite) por defecto. Ajustá `CORS_ALLOWED_ORIGINS` en `settings.py` si tu frontend corre en otro puerto.

## Proyecto relacionado

- Frontend: [RRHH-REACT](https://github.com/brianmatiasllampa/RRHH-REACT)
