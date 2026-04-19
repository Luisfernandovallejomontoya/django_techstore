"""
Elimina todos los RegistroSuelo (útil tras cambiar reglas del semáforo o datos de prueba).

  python manage.py limpiar_registros_suelo --yes
"""

from django.core.management.base import BaseCommand

from agromaker_soil.models import RegistroSuelo


class Command(BaseCommand):
    help = "Borra todos los registros de la tabla agromaker_soil_registrosuelo."

    def add_arguments(self, parser):
        parser.add_argument(
            "--yes",
            action="store_true",
            help="Confirmar borrado sin prompt interactivo.",
        )

    def handle(self, *args, **options):
        if not options["yes"]:
            self.stderr.write(
                "Aborte: ejecute con --yes para confirmar el borrado total.\n"
                "  python manage.py limpiar_registros_suelo --yes"
            )
            return

        n = RegistroSuelo.objects.count()
        RegistroSuelo.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Eliminados {n} registros de suelo."))
