from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def crear_grupos_por_defecto(sender, **kwargs):
    for nombre in ['tecnico', 'supervisor', 'seguridad', 'almacen']:
        Group.objects.get_or_create(name=nombre)
