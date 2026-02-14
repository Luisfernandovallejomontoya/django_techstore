import os
from pathlib import Path
import dj_database_url

# BASE_DIR es: C:\Users\Administrador\Desktop\TechStoreOneline\django_techstore
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@e^a4@y6e!19!7d8*a^h=0^0^9e99t#1w_#^9c%_b^9a^l9t-m'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'crispy_forms',
    'crispy_bootstrap4',
    
    'productos.apps.ProductosConfig',
    'usuarios',
    'pedidos',
    'publicidad_ia.apps.PublicidadIaConfig',
    'agromaker_ai',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_techstore.urls'

# --- CAMBIO CRÍTICO AQUÍ ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Usamos BASE_DIR / 'templates' para asegurar compatibilidad con Windows
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'productos.context_processors.carrito_procesador',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_techstore.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# --- CONFIGURACIÓN DE ESTÁTICOS ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Almacenamiento optimizado
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CART_SESSION_ID = 'carrito'
LOGOUT_REDIRECT_URL = 'catalogo'
LOGIN_REDIRECT_URL = 'catalogo'