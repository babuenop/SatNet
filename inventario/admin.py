from django.contrib import admin
from django.forms import RadioSelect
from .models import ActaEntrega

@admin.register(ActaEntrega)
class ActaEntregaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fecha',
        'tipo',
        'tecnico',
        'cerrado_por',
        'cerrado_en',
        'cerrada_por_tecnico',
        'estado',
    ]
    list_filter = ['tipo', 'estado', 'cerrada_por_tecnico']
    search_fields = ['tecnico__username', 'cerrado_por__username']
    ordering = ['-fecha']

    formfield_overrides = {
        ActaEntrega._meta.get_field('tipo').__class__: {'widget': RadioSelect}
    }
