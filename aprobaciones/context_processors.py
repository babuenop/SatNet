from .models import Aprobacion
from inventario.models import ActaEntrega
from django.contrib.contenttypes.models import ContentType

def aprobaciones_pendientes(request):
    if not request.user.is_authenticated or not request.user.groups.exists():
        return {}

    grupo = request.user.groups.first().name
    pendientes = 0

    for acta in ActaEntrega.objects.filter(firmada_por_tecnico=True):
        ct = ContentType.objects.get_for_model(acta)
        aprobacion = Aprobacion.objects.filter(content_type=ct, object_id=acta.id, tipo=grupo).first()
        if not aprobacion or aprobacion.estado == 'pendiente':
            pendientes += 1

    return {
        'aprobaciones_pendientes_count': pendientes
    }
