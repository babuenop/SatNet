from django.db import models
from django.contrib.auth.models import User  # Solo si manejas usuarios internos

class Material(models.Model):
    codigo = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=100)
    
    proveedor = models.CharField(max_length=50, null=True, blank=True)
    
    activo = models.BooleanField(default=True)  # ← nuevo
    # Si luego creas un modelo Proveedor, puedes reemplazar esto:
    # proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True, blank=True)

    estado = models.CharField(
        max_length=20,
        choices=[
            ('nuevo', 'Nuevo'),
            ('usado', 'Usado'),
            ('dañado', 'Dañado'),
            ('otro', 'Otro'),
        ]
    )

    stock = models.PositiveIntegerField(default=0)
    unidad = models.CharField(max_length=10, default='und')  # und, kg, lt, etc.

    #creado_por = models.ForeignKey(User, related_name='materiales_creados', on_delete=models.SET_NULL, null=True, blank=True)
    #actualizado_por = models.ForeignKey(User, related_name='materiales_actualizados', on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'materiales'
        ordering = ['codigo']
        indexes = [
            models.Index(fields=['estado']),
            models.Index(fields=['unidad']),
        ]

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'

    def save(self, *args, **kwargs):
        # Protección básica para evitar stock negativo si llega por error
        if self.stock < 0:
            self.stock = 0
        super().save(*args, **kwargs)



class ActaEntrega(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tecnico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firmada_por_tecnico = models.BooleanField(default=False)

    def __str__(self):
        return f"Acta #{self.id} - {self.fecha}"


class DetalleEntrega(models.Model):
    acta = models.ForeignKey(ActaEntrega, on_delete=models.CASCADE, related_name='detalles')
    material = models.ForeignKey('Material', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    reparado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.material.descripcion} - {self.cantidad}"
