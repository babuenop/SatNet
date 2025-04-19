# aprobaciones/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.contrib import messages

from inventario.models import ActaEntrega
from .models import Aprobacion
from .forms import ComentarioAprobacionForm
from aprobaciones.utils import obtener_etapa_usuario

from django.http import HttpResponseForbidden



# Constante de flujo de aprobación
FLUJO_ETAPAS = ['tecnico', 'supervisor', 'seguridad', 'almacen']

# -------------------------------------
# 🔄 FUNCIONES AUXILIARES
# -------------------------------------

def etapas_previas(tipo_actual):
    try:
        idx = FLUJO_ETAPAS.index(tipo_actual)
        return FLUJO_ETAPAS[:idx]
    except ValueError:
        return []


def validar_etapas_previas(content_type, object_id, tipo):
    for etapa in etapas_previas(tipo):
        if not Aprobacion.objects.filter(
            tipo=etapa,
            content_type=content_type,
            object_id=object_id,
            estado='aprobado'
        ).exists():
            return etapa  # Retorna la primera etapa faltante
    return None

# -------------------------------------
# ✅ APROBAR OBJETO
# -------------------------------------

@login_required
def aprobar_objeto(request, tipo, app_label, model, object_id):
    model_class = ContentType.objects.get(app_label=app_label, model=model).model_class()
    objeto = get_object_or_404(model_class, pk=object_id)
    content_type = ContentType.objects.get_for_model(objeto)

    # ❗ Validación de rol (grupo debe coincidir con tipo)
    grupos_usuario = [g.name.lower() for g in request.user.groups.all()]
    if tipo.lower() not in grupos_usuario:
        return HttpResponseForbidden("⛔ No tienes permiso para aprobar como esta etapa.")

    # ❗ Validación de etapas previas
    etapa_faltante = validar_etapas_previas(content_type, objeto.id, tipo)
    if etapa_faltante:
        messages.error(request, f"No puedes aprobar como '{tipo.upper()}'. Falta aprobación de: '{etapa_faltante.upper()}'.")
        return redirect(request.GET.get("next", "/"))

    if request.method == 'POST':
        form = ComentarioAprobacionForm(request.POST)
        if form.is_valid():
            aprobacion, _ = Aprobacion.objects.get_or_create(
                tipo=tipo,
                content_type=content_type,
                object_id=objeto.id
            )
            aprobacion.estado = 'aprobado'
            aprobacion.comentario = form.cleaned_data['comentario']
            aprobacion.usuario = request.user
            aprobacion.save()
            messages.success(request, f"Aprobación registrada correctamente como {tipo.upper()}.")
            return redirect(reverse('aprobaciones:mis_aprobaciones'))

    return redirect(request.GET.get("next", "/"))


# -------------------------------------
# ❌ RECHAZAR OBJETO
# -------------------------------------

@login_required
def rechazar_objeto(request, tipo, app_label, model, object_id):
    model_class = ContentType.objects.get(app_label=app_label, model=model).model_class()
    objeto = get_object_or_404(model_class, pk=object_id)
    content_type = ContentType.objects.get_for_model(objeto)

    aprobacion, _ = Aprobacion.objects.get_or_create(
        tipo=tipo,
        content_type=content_type,
        object_id=objeto.id
    )

    etapa_faltante = validar_etapas_previas(content_type, objeto.id, tipo)
    if etapa_faltante:
        messages.error(request, f"No puedes rechazar como '{tipo.upper()}'. Falta aprobación de: '{etapa_faltante.upper()}'.")
        return redirect(request.GET.get("next", "/"))

    if request.method == 'POST':
        form = ComentarioAprobacionForm(request.POST)
        if form.is_valid():
            aprobacion.estado = 'rechazado'
            aprobacion.comentario = form.cleaned_data['comentario']
            aprobacion.usuario = request.user
            aprobacion.save()
            
            # 🔥 Eliminar aprobaciones anteriores
            etapas_anteriores = etapas_previas(tipo)
            Aprobacion.objects.filter(
            content_type=content_type,
            object_id=objeto.id,
            tipo__in=etapas_anteriores
            ).delete()
            
            if hasattr(objeto, 'estado'):
                objeto.estado = 'rechazada'
                objeto.save()

            messages.success(request, f"Aprobación registrada como RECHAZADO por {tipo.upper()}. Se eliminaron aprobaciones anteriores.")
            return redirect(reverse('aprobaciones:mis_aprobaciones'))

    return redirect(request.GET.get("next", "/"))

# -------------------------------------
# 📋 LISTADO DE APROBACIONES PENDIENTES
# -------------------------------------

@login_required
def mis_aprobaciones(request):
    tipo = obtener_etapa_usuario(request.user)
    aprobaciones = Aprobacion.objects.filter(usuario=request.user, estado='pendiente')
    if not tipo:
        return render(request, 'aprobaciones/sin_grupo.html')

    aprobaciones_pendientes = []

    for acta in ActaEntrega.objects.filter(cerrada_por_tecnico=True):
        content_type = ContentType.objects.get_for_model(acta)

        aprobaciones = Aprobacion.objects.filter(
            content_type=content_type,
            object_id=acta.id
        ).values("tipo", "estado")

        estado_etapas = {a["tipo"]: a["estado"] for a in aprobaciones}

        etapas_previas_ok = all(
            estado_etapas.get(etapa) == 'aprobado'
            for etapa in etapas_previas(tipo)
        )
        if not etapas_previas_ok:
            continue

        aprobacion = estado_etapas.get(tipo)
        if not aprobacion or aprobacion == 'pendiente':
            aprobaciones_pendientes.append({
                'objeto': acta,
                'modelo': 'actaentrega',
                'app': 'inventario',
            })
    return render(request, 'aprobaciones/lista_aprobaciones.html', {
        'pendientes': aprobaciones_pendientes,
        'tipo': tipo,
    })
