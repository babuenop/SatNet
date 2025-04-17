from django.core.management.base import BaseCommand
from inventario.models import Material, ActaEntrega, DetalleEntrega

class Command(BaseCommand):
    help = 'Valida integridad básica de los datos en inventario'

    def handle(self, *args, **options):
        errores = 0

        # Materiales sin código o sin descripción
        sin_codigo = Material.objects.filter(codigo__isnull=True) | Material.objects.filter(codigo='')
        sin_desc = Material.objects.filter(descripcion__isnull=True) | Material.objects.filter(descripcion='')

        if sin_codigo.exists():
            errores += sin_codigo.count()
            self.stdout.write(self.style.WARNING(f"⚠️  Materiales sin código: {sin_codigo.count()}"))

        if sin_desc.exists():
            errores += sin_desc.count()
            self.stdout.write(self.style.WARNING(f"⚠️  Materiales sin descripción: {sin_desc.count()}"))

        # Detalles con cantidad inválida
        cantidad_invalidas = DetalleEntrega.objects.filter(cantidad__lte=0)
        if cantidad_invalidas.exists():
            errores += cantidad_invalidas.count()
            self.stdout.write(self.style.WARNING(f"⚠️  Detalles con cantidad <= 0: {cantidad_invalidas.count()}"))

        # Detalles sin reparador
        sin_reparador = DetalleEntrega.objects.filter(reparado_por__isnull=True)
        if sin_reparador.exists():
            errores += sin_reparador.count()
            self.stdout.write(self.style.WARNING(f"⚠️  Detalles sin reparador: {sin_reparador.count()}"))

        # Actas sin técnico o sin detalles
        sin_tecnico = ActaEntrega.objects.filter(tecnico__isnull=True)
        sin_detalles = [a for a in ActaEntrega.objects.all() if not a.detalles.exists()]

        if sin_tecnico.exists():
            errores += sin_tecnico.count()
            self.stdout.write(self.style.WARNING(f"⚠️  Actas sin técnico: {sin_tecnico.count()}"))

        if sin_detalles:
            errores += len(sin_detalles)
            self.stdout.write(self.style.WARNING(f"⚠️  Actas sin detalles: {len(sin_detalles)}"))

        if errores == 0:
            self.stdout.write(self.style.SUCCESS("✅ Todos los datos están en buen estado."))
        else:
            self.stdout.write(self.style.ERROR(f"❌ Se encontraron {errores} problemas de integridad."))
