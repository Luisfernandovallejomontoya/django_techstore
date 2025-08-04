# django_techstore/settings.py

from pathlib import Path

# ==============================================================================
# CONFIGURACIÓN BÁSICA DEL PROYECTO
# ------------------------------------------------------------------------------
# Esta sección define los ajustes fundamentales para el funcionamiento de tu proyecto Django.
# ==============================================================================

# BASE_DIR: Construye rutas dentro del proyecto. Es la raíz de tu proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: Clave secreta única para tu instalación de Django.
# ¡ADVERTENCIA DE SEGURIDAD!: Mantener esta clave en secreto, especialmente en producción.
SECRET_KEY = 'django-insecure-=numplulyb^$!4s8ril!*7%086))8#t82kp0^n+&xajo&9ifn)'

# DEBUG: Modo de depuración.
# True: Habilita mensajes de error detallados y permite servir archivos estáticos/media en desarrollo.
# False: Deshabilita el modo de depuración. ¡Siempre debe ser False en producción por seguridad!
DEBUG = True

# ALLOWED_HOSTS: Lista de cadenas que representan los nombres de host/dominios que puede servir esta instancia de Django.
# En desarrollo (DEBUG=True), generalmente se puede dejar vacío o con 'localhost', '127.0.0.1'.
# En producción, debes listar los dominios reales (ej. ['tutiendaonline.com', 'www.tutiendaonline.com']).
ALLOWED_HOSTS = []


# ==============================================================================
# DEFINICIÓN DE APLICACIONES INSTALADAS (INSTALLED_APPS)
# ------------------------------------------------------------------------------
# Aquí registras todas las aplicaciones (apps) que forman parte de tu proyecto Django.
# Cada aplicación suele tener su propio 'models.py', 'views.py', 'admin.py', etc.
# ==============================================================================

INSTALLED_APPS = [
    # Aplicaciones CORE de Django: Son módulos esenciales que proporcionan funcionalidades básicas.
    'django.contrib.admin',        # Panel de administración de Django.
    'django.contrib.auth',         # Sistema de autenticación de usuarios.
    'django.contrib.contenttypes', # Marcos para tipos de contenido.
    'django.contrib.sessions',     # Gestión de sesiones.
    'django.contrib.messages',     # Sistema de mensajes (para notificaciones al usuario).
    'django.contrib.staticfiles',  # Gestión de archivos estáticos (CSS, JS, imágenes fijas).

    # Tus aplicaciones personalizadas: Son las apps que tú creas para la funcionalidad específica de tu proyecto.
    'productos', # Tu aplicación principal para gestionar productos y el carrito.
                 # Asegúrate de que el nombre aquí ('productos') coincida con el nombre de tu carpeta de app.
]


# ==============================================================================
# MIDDLEWARE
# ------------------------------------------------------------------------------
# El Middleware es un framework de "ganchos" ligero para el procesamiento de peticiones y respuestas.
# Cada componente de middleware realiza alguna función durante la fase de petición/respuesta.
# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # Mejora la seguridad del sitio.
    'django.contrib.sessions.middleware.SessionMiddleware',  # Habilita el soporte de sesiones.
    'django.middleware.common.CommonMiddleware',             # Normas comunes de Django.
    'django.middleware.csrf.CsrfViewMiddleware',             # Protección contra ataques CSRF.
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Asocia usuarios a las peticiones usando sesiones.
    'django.contrib.messages.middleware.MessageMiddleware',  # Permite mensajes de una sola vez.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',# Protección contra clickjacking.
]


# ==============================================================================
# CONFIGURACIÓN DE URLS Y TEMPLATES (PLANTILLAS)
# ------------------------------------------------------------------------------
# Define cómo Django mapea las URLs a las vistas y cómo carga las plantillas HTML.
# ==============================================================================

# ROOT_URLCONF: Especifica el módulo de Python donde Django buscará la configuración de URL raíz.
ROOT_URLCONF = 'django_techstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: Lista de directorios donde Django buscará plantillas adicionales a nivel de proyecto.
        # Si tienes una carpeta 'templates' en la raíz de tu proyecto, la añadirías aquí:
        # 'DIRS': [BASE_DIR / 'templates'],
        'DIRS': [], 
        
        # APP_DIRS: Si es True, Django buscará una subcarpeta 'templates' dentro de cada aplicación registrada.
        # Esto es crucial para que Django encuentre tus plantillas como 'productos/index.html'.
        'APP_DIRS': True, 
        'OPTIONS': {
            'context_processors': [
                # Context processors: Funciones que añaden datos al contexto de la plantilla en cada renderizado.
                'django.template.context_processors.debug',    # Añade variables de depuración (útil con DEBUG=True).
                'django.template.context_processors.request',  # Acceso al objeto 'request' en las plantillas.
                'django.contrib.auth.context_processors.auth', # Permite acceder a 'user' y 'perms' en plantillas.
                'django.contrib.messages.context_processors.messages', # Permite acceder a los mensajes en plantillas.
                # ¡IMPORTANTE!: Procesador de contexto para el carrito de compras.
                # Esto permite que la instancia del carrito esté disponible en TODAS tus plantillas,
                # para mostrar, por ejemplo, el número de ítems en el carrito en la barra de navegación.
                'productos.context_processors.carrito_context', 
            ],
        },
    },
]

# WSGI_APPLICATION: El punto de entrada para servidores WSGI compatibles.
WSGI_APPLICATION = 'django_techstore.wsgi.application'


# ==============================================================================
# CONFIGURACIÓN DE BASE DE DATOS
# ------------------------------------------------------------------------------
# Define la configuración para la conexión a tu base de datos.
# Por defecto, Django usa SQLite para proyectos pequeños y desarrollo.
# ==============================================================================

# DEFAULT_AUTO_FIELD: Tipo de campo de clave primaria predeterminado para modelos sin uno explícito.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Motor de base de datos (SQLite en este caso).
        'NAME': BASE_DIR / 'db.sqlite3',       # Nombre y ruta del archivo de la base de datos.
        'TEST': { # Configuración para la base de datos de pruebas.
            'NAME': BASE_DIR / 'db_test.sqlite3'
        }
    }
}


# ==============================================================================
# AUTENTICACIÓN Y VALIDACIÓN DE CONTRASEÑAS
# ------------------------------------------------------------------------------
# Define las reglas y configuraciones para el sistema de usuarios y autenticación de Django.
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    # Validadores de contraseña: Aseguran que las contraseñas cumplan ciertos criterios de seguridad.
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# URLs de redirección para el sistema de autenticación de Django.
# LOGIN_REDIRECT_URL: A dónde se redirige al usuario después de iniciar sesión exitosamente.
# Aquí se redirige al catálogo de productos.
LOGIN_REDIRECT_URL = '/productos/catalogo/' 
# LOGOUT_REDIRECT_URL: A dónde se redirige al usuario después de cerrar sesión.
# También se redirige al catálogo de productos.
LOGOUT_REDIRECT_URL = '/productos/catalogo/'


# ==============================================================================
# INTERNACIONALIZACIÓN Y ZONA HORARIA (I18N / L10N)
# ------------------------------------------------------------------------------
# Configuración para el idioma, formato de fecha/hora y zona horaria de tu aplicación.
# ==============================================================================

LANGUAGE_CODE = 'es-co'     # Código de idioma: 'es-co' para español de Colombia.
TIME_ZONE = 'America/Bogota'# Zona horaria: 'America/Bogota' para Colombia.
USE_I18N = True             # Habilita el sistema de internacionalización de Django.
USE_TZ = True               # Habilita el soporte de zonas horarias.


# ==============================================================================
# ARCHIVOS ESTÁTICOS (CSS, JavaScript, Imágenes fijas de la APP)
# ------------------------------------------------------------------------------
# Configuración para servir archivos estáticos que son parte del código de la aplicación
# (ej. tu 'style.css' en 'productos/static/productos/css/').
# ==============================================================================

STATIC_URL = '/static/' # La URL base para referenciar archivos estáticos en las plantillas (ej. {% static 'css/style.css' %}).

# STATICFILES_DIRS: Una lista de directorios adicionales donde Django buscará archivos estáticos.
# Es útil si tienes una carpeta 'static' a nivel de proyecto para archivos globales.
STATICFILES_DIRS = [
    BASE_DIR / 'static', # Ejemplo: apunta a 'tu_proyecto_django/static/'
]

# STATIC_ROOT: La ruta ABSOLUTA donde 'collectstatic' reunirá todos los archivos estáticos
# (tanto de tus apps como de STATICFILES_DIRS) cuando prepares la aplicación para producción.
# ¡No uses esta ruta para desarrollo, solo para producción!
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ==============================================================================
# ARCHIVOS MULTIMEDIA (MEDIA FILES)
# ------------------------------------------------------------------------------
# Configuración para archivos subidos por los usuarios o a través del administrador
# (ej. las imágenes de tus productos que subes en el Admin de Django).
# ==============================================================================

MEDIA_URL = '/media/' # La URL base para referenciar archivos multimedia en las plantillas.
# MEDIA_ROOT: La ruta ABSOLUTA del sistema de archivos donde se almacenarán
# físicamente los archivos multimedia subidos.
MEDIA_ROOT = BASE_DIR / 'media'


# ==============================================================================
# CONFIGURACIÓN ESPECÍFICA DEL CARRITO DE COMPRAS
# ------------------------------------------------------------------------------
# Define la clave para almacenar el carrito en la sesión del usuario.
# ==============================================================================

CART_SESSION_ID = 'carrito' # Nombre de la clave usada en la sesión de Django para el carrito.