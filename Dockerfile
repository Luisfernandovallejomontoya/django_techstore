FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Para producción define SECRET_KEY, DEBUG=False, ALLOWED_HOSTS y (opcional) DATABASE_URL.
# Ejemplo: ejecutar collectstatic antes de arrancar si sirves estáticos desde este contenedor.
CMD ["gunicorn", "django_techstore.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
