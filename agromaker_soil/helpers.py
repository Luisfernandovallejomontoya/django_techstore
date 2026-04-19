"""
Lecturas coherentes de humedad entre modelo, vistas y reportes.

Histórico: el formulario guardaba solo en `conductividad`; el modelo
también tiene `humedad` y la propiedad `interpretacion_ph` usa `humedad`.
Priorizamos `conductividad` si tiene valor (filas viejas), si no `humedad`.
"""


def humedad_coherente(registro) -> float:
    for attr in ("conductividad", "humedad"):
        val = getattr(registro, attr, None)
        if val is None or val == "":
            continue
        try:
            return float(str(val).replace(",", "."))
        except (ValueError, TypeError):
            continue
    return 0.0
