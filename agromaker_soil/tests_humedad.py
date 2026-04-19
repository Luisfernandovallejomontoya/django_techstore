from django.test import TestCase
from agromaker_soil.models import RegistroSuelo 
from agromaker_soil.helpers import humedad_coherente

class HumedadCoherenteTest(TestCase):
    def test_lectura_datos_antiguos(self):
        # Simulamos un registro antiguo (solo conductividad)
        registro = RegistroSuelo(ph=6.0, conductividad=45.5, humedad=0)
        self.assertEqual(humedad_coherente(registro), 45.5)

    def test_lectura_datos_nuevos(self):
        # Simulamos un registro nuevo (sincronizado)
        registro = RegistroSuelo(ph=6.0, conductividad=50.0, humedad=50.0)
        self.assertEqual(humedad_coherente(registro), 50.0)