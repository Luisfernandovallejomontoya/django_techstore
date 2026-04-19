"""
Jerarquía de decisión única para el semáforo de suelos (vista, tarjetas, modelo).

Rangos de pH mutuamente excluyentes (sin solape con umbral 5.5):
  - Rojo (acidez crítica): p < 5.0
  - Amarillo (vigilancia / peligro leve): 5.0 <= p < 6.0
  - Verde (óptimo): 6.0 <= p <= 7.2 y humedad < 70%

Humedad extrema se evalúa antes que bandas de pH solo cuando aplica emergencia.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .helpers import humedad_coherente


@dataclass(frozen=True)
class EstadoSuelo:
    """Una sola fuente de verdad para encabezado, tarjetas y etiquetas."""

    color: str  # rojo | naranja | amarillo | verde | gris
    alerta: str
    recomendacion: str
    etiqueta_tarjeta: str
    color_hex: str


def evaluar_estado_suelo(registro: Optional[object]) -> EstadoSuelo:
    if registro is None:
        return EstadoSuelo(
            color="verde",
            alerta="ESTADO ÓPTIMO",
            recomendacion="Puede proceder con las labores programadas.",
            etiqueta_tarjeta="🟢 Sin lectura reciente — esperando sincronización",
            color_hex="#198754",
        )

    try:
        p = float(registro.ph)
    except (ValueError, TypeError):
        return EstadoSuelo(
            color="gris",
            alerta="ERROR EN DATOS",
            recomendacion="Verifique el registro de pH en el inyector de datos.",
            etiqueta_tarjeta="🔵 ERROR: DATOS",
            color_hex="#6c757d",
        )

    h = humedad_coherente(registro)

    # 1) Emergencia por saturación (prioridad sobre bandas de pH)
    if h > 90.0:
        return EstadoSuelo(
            color="rojo",
            alerta="EMERGENCIA POR SATURACIÓN",
            recomendacion="Evitar tráfico de maquinaria. Drenaje y asesoría técnica urgente.",
            etiqueta_tarjeta="🔴 CRÍTICO: EMERGENCIA (SATURACIÓN)",
            color_hex="#dc3545",
        )

    # 2) Acidez crítica — umbral estricto p < 5.0 (5.4 ya no cae aquí)
    if p < 5.0:
        return EstadoSuelo(
            color="rojo",
            alerta="ALERTA DE ACIDEZ CRÍTICA",
            recomendacion="Aplicar enmienda (cal agrícola) con asesoría técnica urgente.",
            etiqueta_tarjeta="🔴 CRÍTICO: ACIDEZ",
            color_hex="#dc3545",
        )

    # 3) Vigilancia / peligro leve
    if 5.0 <= p < 6.0:
        return EstadoSuelo(
            color="amarillo",
            alerta="PELIGRO LEVE (VIGILANCIA)",
            recomendacion="Monitorear pH. Considerar enmienda preventiva según análisis.",
            etiqueta_tarjeta="⚠️ VIGILANCIA: AMARILLO ⚠️",
            color_hex="#ffc107",
        )

    # 4) Humedad alta sin banda amarilla/roja de pH
    if h > 80.0:
        return EstadoSuelo(
            color="naranja",
            alerta="SATURACIÓN POR LLUVIA",
            recomendacion="Suspender fertilización. Riesgo de lixiviación.",
            etiqueta_tarjeta="🟠 HUMEDAD ALTA: PRECAUCIÓN",
            color_hex="#fd7e14",
        )

    # 5) Óptimo
    if 6.0 <= p <= 7.2 and h < 70.0:
        return EstadoSuelo(
            color="verde",
            alerta="ESTADO ÓPTIMO",
            recomendacion="Puede proceder con las labores programadas.",
            etiqueta_tarjeta="🟢 ÓPTIMO: SUELO SANO",
            color_hex="#198754",
        )

    return EstadoSuelo(
        color="gris",
        alerta="REVISAR: FUERA DE RANGO",
        recomendacion="Valores de pH u humedad fuera de banda operativa. Consulte técnico.",
        etiqueta_tarjeta="⚪ REVISAR: FUERA DE RANGO",
        color_hex="#6c757d",
    )
