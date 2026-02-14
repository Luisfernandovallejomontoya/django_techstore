import os
import sys
import logging
from django.db import models

# Configuración de logs
logger = logging.getLogger(__name__)

# --- EL "GPS" DE RUTAS PARA LA IA ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

try:
    from agromaker_ai.logic.biology import verificar_hipoxia
    from agromaker_ai.logic.geotechnics import evaluar_riesgo_deslizamiento
except ImportError:
    try:
        from .logic.biology import verificar_hipoxia
        from .logic.geotechnics import evaluar_riesgo_deslizamiento
    except ImportError as e:
        logger.error(f"❌ FALLO DE CONEXIÓN CON LOGIC: {e}")
        def verificar_hipoxia(n): return {'estado': 'ERROR', 'mensaje': 'Módulo Biología desconectado'}
        def evaluar_riesgo_deslizamiento(n): return {'riesgo': 'ERROR', 'mensaje': 'Módulo Geotecnia desconectado'}

class PrediccionClimatica(models.Model):
    # Identificación
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_prediccion = models.DateField(verbose_name="Fecha Predicha")

    # Entradas Técnicas
    lluvia_mm = models.FloatField(default=0.0, verbose_name="Lluvia (mm)")
    saturacion_suelo = models.FloatField(default=0.0, verbose_name="Saturación Suelo (mm)")
    temperatura = models.FloatField(default=20.0, verbose_name="Temperatura (°C)")
    humedad = models.FloatField(default=50.0, verbose_name="Humedad (%)")
    lluvia_probable = models.BooleanField(default=False, verbose_name="¿Probabilidad de Lluvia?")
    
    # Clasificación
    nivel_riesgo_plaga = models.CharField(max_length=20, choices=[
        ('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto'),
    ], default='Bajo')
    
    # Salidas de la IA
    analisis_inteligente = models.TextField(blank=True, null=True, verbose_name="Análisis Inteligente")
    semaforo_estado = models.CharField(max_length=10, default='VERDE', editable=False)

    class Meta:
        verbose_name = "Predicción Agromaker"
        verbose_name_plural = "Predicciones Agromaker"
        ordering = ['-fecha_prediccion']

    # --- NUEVA LÓGICA COMERCIAL PEDAGÓGICA ---
    def recomendacion_comercial(self):
        """
        Retorna un diccionario con la recomendación de compra basada en el semáforo.
        """
        if self.semaforo_estado == 'ROJO':
            return {
                "mensaje": "🚨 Suelo saturado. ¡Protege tus raíces!",
                "boton": "Ver Sistemas de Drenaje",
                "link": "/productos/", # Aquí puedes poner el link real a tu categoría
                "color": "danger"
            }
        elif self.semaforo_estado == 'AMARILLO':
            return {
                "mensaje": "⚠️ Alta humedad. Previene hongos y plagas.",
                "boton": "Ver Fungicidas y Botas",
                "link": "/productos/",
                "color": "warning text-dark"
            }
        else:
            return {
                "mensaje": "✅ Clima ideal. Nutre tu cultivo hoy.",
                "boton": "Ver Fertilizantes",
                "link": "/productos/",
                "color": "success"
            }

    def save(self, *args, **kwargs):
        """
        Ejecuta los motores de lógica y garantiza que el análisis nunca esté vacío.
        """
        try:
            res_bio = verificar_hipoxia(self.saturacion_suelo or 0)
            res_geo = evaluar_riesgo_deslizamiento(self.lluvia_mm or 0)

            if res_geo.get('riesgo') == 'ALTO' or res_bio.get('estado') == 'CRITICO':
                self.semaforo_estado = 'ROJO'
                if not self.analisis_inteligente:
                    self.analisis_inteligente = f"🚨 ALERTA CRÍTICA: {res_geo.get('mensaje')}. {res_bio.get('mensaje')}."
            
            elif (self.lluvia_mm or 0) > 50 or (self.saturacion_suelo or 0) > 100:
                self.semaforo_estado = 'AMARILLO'
                if not self.analisis_inteligente:
                    self.analisis_inteligente = "⚠️ PRECAUCIÓN: Suelos saturados. Monitorear drenajes."
            
            else:
                self.semaforo_estado = 'VERDE'
                if not self.analisis_inteligente:
                    self.analisis_inteligente = "✅ CONDICIONES ÓPTIMAS: Suelo oxigenado. Clima favorable."

        except Exception as e:
            self.semaforo_estado = 'GRIS'
            self.analisis_inteligente = f"⚙️ Error de Procesamiento: {str(e)}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fecha_prediccion} | {self.lluvia_mm}mm | {self.semaforo_estado}"