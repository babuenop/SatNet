from django.contrib.contenttypes.models import ContentType
from .models import Aprobacion
from inventario.models import ActaEntrega
from .views import etapas_previas, obtener_etapa_usuario  # si están en views.py

def aprobaciones_pendientes(request):
    if not request.user.is_authenticated:
        return {}

    tipo = obtener_etapa_usuario(request.user)
    if not tipo:
        return {}

    count = 0

    for acta in ActaEntrega.objects.filter(firmada_por_tecnico=True).exclude(estado='rechazada'):
        content_type = ContentType.objects.get_for_model(acta)

        aprobaciones = Aprobacion.objects.filter(
            content_type=content_type,
            object_id=acta.id
        ).values("tipo", "estado")

        estado_etapas = {a["tipo"]: a["estado"] for a in aprobaciones}

        etapas_previas_ok = all(
            estado_etapas.get(etapa) == 'aprobado'
            for etapa in etapas_previas(tipo)
        )
        if not etapas_previas_ok:
            continue

        aprobacion = estado_etapas.get(tipo)
        if not aprobacion or aprobacion == 'pendiente':
            count += 1

    return {
        'aprobaciones_pendientes_count': count
    }
