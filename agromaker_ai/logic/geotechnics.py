def evaluar_riesgo_deslizamiento(lluvia_mm):
    """
    Analiza la estabilidad del terreno basándose en la intensidad de la lluvia.
    """
    if lluvia_mm > 150:
        return {
            'riesgo': 'ALTO',
            'mensaje': 'Peligro de remoción en masa: La intensidad de lluvia supera el umbral de seguridad para laderas.'
        }
    elif lluvia_mm > 80:
        return {
            'riesgo': 'MEDIO',
            'mensaje': 'Suelo inestable: Monitorear grietas en el terreno y flujos de lodo.'
        }
    else:
        return {
            'riesgo': 'BAJO',
            'mensaje': 'Terreno estable: Sin alertas de movimiento de tierra.'
        }