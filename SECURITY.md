# Política de seguridad

## Reporte de vulnerabilidades
Si encuentras una vulnerabilidad de seguridad, evita publicarla en issues abiertos. Contacta a los mantenedores del repositorio por un canal privado y proporciona:
- descripción del problema e impacto,
- pasos para reproducir,
- versión/commit afectado,
- posible mitigación o parche (si lo tienes).

## Buenas prácticas del proyecto
- No versionar secretos (`SECRET_KEY`, credenciales, tokens, `.env`).
- Usar `DEBUG=False` en producción.
- Configurar `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` y opciones `SECURE_*`/HTTPS según el entorno.
- Mantener dependencias actualizadas y revisar avisos de seguridad.
