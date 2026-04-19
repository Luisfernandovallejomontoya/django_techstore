"""
Test de coherencia de datos — Informe Agromaker Soil Monitoring (Filadelfia).

Valida humedad_coherente() con mocks (sin tocar BD ni modelos Django),
evitando dependencias circulares entre helpers y models.
"""

from django.test import TestCase


class HumedadCoherenteTest(TestCase):
    """
    Certificación de integridad: lectura correcta de humedad para
    registros legacy (solo conductividad) y nuevos (campos sincronizados).
    """

    def test_algoritmo_humedad(self):
        from agromaker_soil.helpers import humedad_coherente

        class MockRegistro:
            def __init__(self, cond, hum):
                self.conductividad = cond
                self.humedad = hum

        # A: Legacy — solo conductividad poblada (humedad en 0 por defecto)
        self.assertEqual(humedad_coherente(MockRegistro(45.5, 0)), 45.5)

        # B: Nuevos — ambos campos sincronizados
        self.assertEqual(humedad_coherente(MockRegistro(50.0, 50.0)), 50.0)

    def test_legacy_coma_decimal(self):
        """Conductividad como string con coma (formato de formulario)."""
        from agromaker_soil.helpers import humedad_coherente

        class MockRegistro:
            def __init__(self, cond, hum):
                self.conductividad = cond
                self.humedad = hum

        self.assertEqual(humedad_coherente(MockRegistro("45,5", 0)), 45.5)

    def test_nuevo_solo_humedad(self):
        """Si conductividad vacía, se usa humedad (filas futuras o migración)."""
        from agromaker_soil.helpers import humedad_coherente

        class MockRegistro:
            def __init__(self, cond, hum):
                self.conductividad = cond
                self.humedad = hum

        self.assertEqual(humedad_coherente(MockRegistro(None, 62.3)), 62.3)
