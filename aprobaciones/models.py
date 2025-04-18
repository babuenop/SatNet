# aprobaciones/models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Aprobacion(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]

    tipo = models.CharField(max_length=50)  # ejemplo: 'supervisor', 'seguridad', etc.
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    comentario = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='aprobaciones_realizadas')

    # Soporte genérico
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    contenido = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('tipo', 'content_type', 'object_id')
