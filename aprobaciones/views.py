# aprobaciones/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Aprobacion
from .forms import ComentarioAprobacionForm

def aprobar_objeto(request, tipo, app_label, model, object_id):
    model_class = ContentType.objects.get(app_label=app_label, model=model).model_class()
    objeto = get_object_or_404(model_class, pk=object_id)
    aprobacion, _ = Aprobacion.objects.get_or_create(
        tipo=tipo,
        content_type=ContentType.objects.get_for_model(objeto),
        object_id=objeto.id
    )
    if request.method == 'POST':
        form = ComentarioAprobacionForm(request.POST)
        if form.is_valid():
            aprobacion.estado = 'aprobado'
            aprobacion.comentario = form.cleaned_data['comentario']
            aprobacion.usuario = request.user
            aprobacion.save()
        return redirect(request.GET.get('next', '/'))  # <= asegúrate que esto esté aquí

    # Si entra por GET, no renderices nada, siempre redirige
    return redirect(request.GET.get('next', '/'))


def rechazar_objeto(request, tipo, app_label, model, object_id):
    model_class = ContentType.objects.get(app_label=app_label, model=model).model_class()
    objeto = get_object_or_404(model_class, pk=object_id)
    aprobacion, _ = Aprobacion.objects.get_or_create(
        tipo=tipo,
        content_type=ContentType.objects.get_for_model(objeto),
        object_id=objeto.id
    )
    if request.method == 'POST':
        form = ComentarioAprobacionForm(request.POST)
        if form.is_valid():
            aprobacion.estado = 'rechazado'
            aprobacion.comentario = form.cleaned_data['comentario']
            aprobacion.usuario = request.user
            aprobacion.save()
        return redirect(request.GET.get('next', '/'))  # <= asegúrate que esto esté aquí

    # Si entra por GET, no renderices nada, siempre redirige
    return redirect(request.GET.get('next', '/'))
