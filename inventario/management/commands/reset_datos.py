from django.core.management.base import BaseCommand
from inventario.models import ActaEntrega, DetalleEntrega, Material

class Command(BaseCommand):
    help = 'Elimina todos los registros de materiales y entregas'

    def handle(self, *args, **options):
        DetalleEntrega.objects.all().delete()
        ActaEntrega.objects.all().delete()
        Material.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("✅ Todos los datos fueron eliminados."))
