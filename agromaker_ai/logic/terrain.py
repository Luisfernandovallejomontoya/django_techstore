# terrain.py - Especialista en Topografía y Drenaje

def verificar_ventana_trabajo(horas_sin_lluvia, inclinacion_lote):
    """
    PUNTO 5: Determina si el suelo ya drenó lo suficiente.
    inclinacion_lote: 'plano', 'moderado', 'pendiente_fuerte'
    """
    # En Pereira (laderas), el drenaje es más lento si el suelo está saturado
    tiempo_minimo = 24 # horas estándar
    
    if inclinacion_lote == 'pendiente_fuerte':
        tiempo_minimo = 36 # Requiere más tiempo para estabilizarse
    
    if horas_sin_lluvia < tiempo_minimo:
        return {
            "apto": False,
            "motivo": f"Suelo aún en proceso de drenaje. Espere a cumplir {tiempo_minimo}h."
        }
    return {"apto": True, "motivo": "Suelo con humedad estable para labores."}