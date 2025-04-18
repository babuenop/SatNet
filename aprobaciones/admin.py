from django.contrib import admin
from .models import Aprobacion

@admin.register(Aprobacion)
class AprobacionAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'estado', 'usuario', 'fecha', 'content_type', 'object_id')
    list_filter = ('estado', 'tipo', 'fecha')
    search_fields = ('comentario', 'usuario__username')
