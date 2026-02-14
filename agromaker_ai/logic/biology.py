def verificar_hipoxia(saturacion_suelo):
    """
    Determina el estado de oxigenación de las raíces basado en la saturación.
    """
    if saturacion_suelo > 200:
        return {
            'estado': 'CRITICO',
            'mensaje': 'Suelo saturado: Riesgo inminente de hipoxia radicular (asfixia de raíces).'
        }
    elif saturacion_suelo > 150:
        return {
            'estado': 'ADVERTENCIA',
            'mensaje': 'Suelo muy húmedo: Reducción de intercambio gaseoso detectada.'
        }
    else:
        return {
            'estado': 'NORMAL',
            'mensaje': 'Niveles de oxígeno en suelo óptimos.'
        }