from django.contrib.contenttypes.models import ContentType
from .models import Aprobacion
from inventario.models import ActaEntrega



FLUJO_ETAPAS = ['tecnico', 'supervisor', 'seguridad', 'almacen']


def etapas_previas(tipo_actual):
    try:
        idx = FLUJO_ETAPAS.index(tipo_actual)
        return FLUJO_ETAPAS[:idx]
    except ValueError:
        return []


def obtener_etapa_usuario(user):
    GRUPO_ETAPA = {
        "tecnico": "tecnico",
        "supervisor": "supervisor",
        "seguridad": "seguridad",
        "almacen": "almacen",
    }

    grupos = user.groups.values_list("name", flat=True)
    print("DEBUG grupos en utils.py:", list(grupos))  # 👈 Agrega esto para ver si se ejecuta

    for grupo in grupos:
        grupo_lower = grupo.lower().strip()
        if grupo_lower in GRUPO_ETAPA:
            return GRUPO_ETAPA[grupo_lower]

    return None


def obtener_aprobaciones_pendientes(user):
    from .views import etapas_previas, obtener_etapa_usuario  # si están en views
    tipo = obtener_etapa_usuario(user)
    if not tipo:
        return []

    pendientes = []

    for acta in ActaEntrega.objects.filter(firmada_por_tecnico=True):
        content_type = ContentType.objects.get_for_model(acta)
        aprobaciones = Aprobacion.objects.filter(
            content_type=content_type,
            object_id=acta.id
        ).values("tipo", "estado")
        estado_etapas = {a["tipo"]: a["estado"] for a in aprobaciones}

        etapas_ok = all(
            estado_etapas.get(e) == "aprobado"
            for e in etapas_previas(tipo)
        )
        if not etapas_ok:
            continue

        estado_actual = estado_etapas.get(tipo)
        if not estado_actual or estado_actual == "pendiente":
            pendientes.append(acta)

    return pendientes






def obtener_etapa_pendiente(acta):
    content_type = ContentType.objects.get_for_model(acta)
    aprobaciones = {
        a.tipo: a.estado for a in Aprobacion.objects.filter(content_type=content_type, object_id=acta.id)
    }
    for etapa in FLUJO_ETAPAS:
        if aprobaciones.get(etapa) != 'aprobado':
            return etapa
    return None
