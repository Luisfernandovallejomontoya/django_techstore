# TechStore Online + Agromaker AI

Aplicación web en **Django** que integra un módulo de **comercio electrónico** (catálogo, carrito, pedidos y usuarios) con módulos **Agromaker AI / Agromaker Soil** orientados a monitoreo y apoyo a decisiones agrícolas (Filadelfia, Caldas).

> Este repositorio contiene una evolución activa del proyecto. Algunas funcionalidades avanzadas descritas en hitos previos (p. ej. reportes PDF/Excel específicos, integraciones IoT o dashboards concretos) dependen de la implementación y configuración disponible en cada módulo/rama.

## Características principales

### E-commerce
- Navegación de productos y catálogo.
- Carrito de compras basado en sesión (`CART_SESSION_ID`).
- Gestión de pedidos (modelos de pedido y detalle) y panel de administración de Django.
- Autenticación de usuarios y rutas de gestión relacionadas.
- Formularios con `django-crispy-forms` + Bootstrap 4.

### Agromaker (IA / suelos)
- Módulos `agromaker_ai` y `agromaker_soil` integrados en el proyecto.
- Rutas dedicadas: `/agromaker/` y `/suelos/` (además del hub principal en `/`).
- Lógica de interpretación de pH y registro de suelo en `agromaker_soil` (ej. clasificación ácido/óptimo/alcalino).

## Stack técnico
- **Backend:** Django 5.x
- **Base de datos:** SQLite por defecto; soporta `DATABASE_URL` (vía `dj-database-url`)
- **Frontend:** Bootstrap 4, plantillas Django
- **Estáticos:** WhiteNoise
- **Servidor de aplicación (contenedor/prod):** Gunicorn
- **Datos/reportes (según módulos):** pandas, numpy, openpyxl, xhtml2pdf

## Estructura del repositorio (resumen)
- `django_techstore/` — configuración del proyecto (`settings.py`, `urls.py`, `wsgi.py`, etc.)
- `productos/`, `usuarios/`, `pedidos/`, `publicidad_ia/` — apps de e-commerce/soporte
- `agromaker_ai/`, `agromaker_soil/` — módulos agro/IA
- `templates/`, `staticfiles/`, `media/` — recursos de plantilla y archivos (según entorno)
- `Dockerfile`, `requirements.txt`, `.env.example`

## Requisitos previos
- Python 3.11+ (recomendado)
- `pip` y entorno virtual (`venv`)
- (Opcional) Docker

## Instalación y ejecución local

### 1. Clonar e ingresar al proyecto
```bash
git clone https://github.com/Luisfernandovallejomontoya/django_techstore.git
cd django_techstore
```

### 2. Crear y activar entorno virtual
**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Copia `.env.example` como `.env` (o define las variables en tu entorno) y ajusta los valores:

- `SECRET_KEY`: clave secreta de Django (obligatoria fuera de desarrollo local)
- `DEBUG`: `True`/`False`
- `ALLOWED_HOSTS`: hosts permitidos separados por coma
- `CSRF_TRUSTED_ORIGINS`: orígenes confiables para CSRF (si aplica)
- `DATABASE_URL` (opcional): cadena de conexión a base de datos externa

### 5. Migraciones y usuario administrador
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Ejecutar en desarrollo
```bash
python manage.py runserver
```
Aplicación: `http://127.0.0.1:8000/` · Admin: `http://127.0.0.1:8000/admin/`

## Ejecución con Docker

```bash
docker build -t django-techstore .
docker run --rm -p 8000:8000 \
  -e SECRET_KEY="cambia-esta-clave" \
  -e DEBUG=False \
  -e ALLOWED_HOSTS="localhost,127.0.0.1" \
  django-techstore
```

> Notas: el contenedor arranca con Gunicorn. Para servir archivos estáticos en producción, ejecuta `python manage.py collectstatic` como parte de tu flujo de despliegue/build según tu plataforma. Si usas base de datos externa, proporciona `DATABASE_URL`.

## Rutas relevantes
- `/` — hub principal (`hub_agromaker`)
- `/admin/` — administración de Django
- `/productos/`, `/usuarios/`, `/pedidos/` — módulos de e-commerce
- `/agromaker/` — rutas del módulo `agromaker_ai` (p. ej. `semaforo/`, `dashboard/`, `mapa-satelital/`, `exportar/`)
- `/suelos/` — rutas del módulo `agromaker_soil`

## Buenas prácticas y seguridad
- No subas `.env`, `db.sqlite3`, archivos `media/` sensibles ni artefactos generados.
- Usa `DEBUG=False`, un `SECRET_KEY` fuerte y `ALLOWED_HOSTS`/`CSRF_TRUSTED_ORIGINS` correctos en producción.
- Revisa dependencias y configuración antes de desplegar.

## Estado
Proyecto en evolución (e-commerce + módulos Agromaker). Se recomienda ejecutar `python manage.py check` y pruebas del proyecto en un entorno limpio tras instalar dependencias.

## Licencia
Este proyecto se distribuye bajo la licencia **MIT**. Consulta el archivo [`LICENSE`](LICENSE) para más detalles.
