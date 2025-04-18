# aprobaciones/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.contenttypes.models import ContentType
from inventario.models import ActaEntrega
from .models import Aprobacion
from .forms import ComentarioAprobacionForm
from django.urls import reverse

from .utils import etapas_previas
from django.contrib import messages


# 🚨 Aprobación de objeto

def aprobar_objeto(request, tipo, app_label, model, object_id):
    model_class = ContentType.objects.get(app_label=app_label, model=model).model_class()
    objeto = get_object_or_404(model_class, pk=object_id)
    content_type = ContentType.objects.get_for_model(objeto)

    aprobacion, _ = Aprobacion.objects.get_or_create(
        tipo=tipo,
        content_type=content_type,
        object_id=objeto.id
    )

    # 🚨 Validación de etapas anteriores
    for etapa in etapas_previas(tipo):
        previa = Aprobacion.objects.filter(
            tipo=etapa,
            content_type=content_type,
            object_id=objeto.id,
            estado='aprobado'
        ).first()
        if not previa:
            messages.error(request, f"No puedes aprobar como '{tipo.upper()}'. Aún falta la aprobación de: '{etapa.upper()}'.")
            return redirect(request.GET.get("next", "/"))

    if request.method == 'POST':
        form = ComentarioAprobacionForm(request.POST)
        if form.is_valid():
            aprobacion.estado = 'aprobado'
            aprobacion.comentario = form.cleaned_data['comentario']
            aprobacion.usuario = request.user
            aprobacion.save()
            messages.success(request, f"Aprobación registrada correctamente como {tipo.upper()}.")
        return redirect(reverse('aprobaciones:mis_aprobaciones'))

    return redirect(request.GET.get('next', '/'))

# 🚨 Rechazo de objeto

def rechazar_objeto(request, tipo, app_label, model, object_id):
    model_class = ContentType.objects.get(app_label=app_label, model=model).model_class()
    objeto = get_object_or_404(model_class, pk=object_id)
    content_type = ContentType.objects.get_for_model(objeto)

    aprobacion, _ = Aprobacion.objects.get_or_create(
        tipo=tipo,
        content_type=content_type,
        object_id=objeto.id
    )

    # 🚨 Validación de flujo de etapas previas
    for etapa in etapas_previas(tipo):
        previa = Aprobacion.objects.filter(
            tipo=etapa,
            content_type=content_type,
            object_id=objeto.id,
            estado='aprobado'
        ).first()
        if not previa:
            messages.error(request, f"No puedes rechazar como '{tipo.upper()}'. Falta aprobación de: '{etapa.upper()}'.")
            return redirect(request.GET.get("next", "/"))

    if request.method == 'POST':
        form = ComentarioAprobacionForm(request.POST)
        if form.is_valid():
            aprobacion.estado = 'rechazado'
            aprobacion.comentario = form.cleaned_data['comentario']
            aprobacion.usuario = request.user
            aprobacion.save()
            messages.success(request, f"Aprobación registrada como RECHAZADO por {tipo.upper()}.")
        return redirect(reverse('aprobaciones:mis_aprobaciones'))

    return redirect(request.GET.get('next', '/'))

  # Aquí podés agregar más modelos luego

@login_required
def mis_aprobaciones(request):
    grupo = request.user.groups.first()
    if not grupo:
        return render(request, 'aprobaciones/sin_grupo.html')

    tipo = grupo.name
    aprobaciones_pendientes = []

    # ACTAS DE ENTREGA — se puede extender a otros modelos fácilmente
    for acta in ActaEntrega.objects.filter(firmada_por_tecnico=True):
        content_type = ContentType.objects.get_for_model(acta)
        aprobacion = Aprobacion.objects.filter(
            content_type=content_type,
            object_id=acta.id,
            tipo=tipo
        ).first()
        if not aprobacion or aprobacion.estado == 'pendiente':
            aprobaciones_pendientes.append({
                'objeto': acta,
                'modelo': 'actaentrega',
                'app': 'inventario',
            })

    return render(request, 'aprobaciones/lista_aprobaciones.html', {
        'pendientes': aprobaciones_pendientes,
        'tipo': tipo,
    })
