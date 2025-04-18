from django.db import models

class DocumentoDemo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
