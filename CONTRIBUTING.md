# Contribuir

Gracias por tu interés en contribuir a este proyecto.

## Flujo básico
1. Crea un fork y una rama desde `main`.
2. Configura tu entorno local (ver `README.md`) y copia `.env.example` según corresponda.
3. Realiza cambios pequeños y enfocados.
4. Ejecuta verificaciones antes de abrir un PR:
   - `python manage.py check`
   - `python manage.py test`
   - `python manage.py collectstatic --noinput` (si aplica a tu cambio)
5. Abre un Pull Request describiendo el problema, la solución y cómo probarlo.

## Convenciones
- Mantén la configuración sensible fuera del repositorio (`.env`, claves, credenciales).
- No incluyas artefactos generados (`db.sqlite3`, `staticfiles/`, `media/` locales, etc.).
- Prioriza compatibilidad con la estructura actual del proyecto y cambios claros.

## Reporte de problemas
Incluye pasos para reproducir, comportamiento esperado/actual, entorno (SO, versión de Python/Django) y logs relevantes.
