from .models import Aprobacion
from django.contrib.contenttypes.models import ContentType

def obtener_dict_aprobaciones(objeto):
    """Devuelve un diccionario con las aprobaciones por tipo para el objeto dado"""
    content_type = ContentType.objects.get_for_model(objeto)
    aprobaciones = Aprobacion.objects.filter(
        content_type=content_type,
        object_id=objeto.id
    )
    return {a.tipo: a for a in aprobaciones}
