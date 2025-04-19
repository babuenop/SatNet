 # Usuario por defecto de Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from .models import ActaEntrega, DetalleEntrega, Material
from .forms import MaterialForm

from aprobaciones.models import Aprobacion
from aprobaciones.utils import FLUJO_ETAPAS, etapas_previas, obtener_etapa_pendiente
from aprobaciones.helpers import obtener_dict_aprobaciones
from aprobaciones.views import obtener_etapa_usuario


# ---------- CRUD MATERIALES ----------

@login_required
def lista_materiales(request):
    materiales = Material.objects.all()

    # Marcar si el material aparece en una acta firmada
    for material in materiales:
        material.tiene_acta_firmada = DetalleEntrega.objects.filter(
            material=material,
            acta__firmada_por_tecnico=True
        ).exists()

    return render(request, 'inventario/lista.html', {'materiales': materiales})


@login_required
def crear_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.creado_por = request.user
            material.actualizado_por = request.user
            material.save()
            return redirect('inventario:lista_materiales')
    else:
        form = MaterialForm()
    return render(request, 'inventario/formulario.html', {'form': form})


@login_required
def editar_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            material = form.save(commit=False)
            material.actualizado_por = request.user
            material.save()
            return redirect('inventario:lista_materiales')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'inventario/formulario.html', {'form': form})


@login_required
def eliminar_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('inventario:lista_materiales')
    return render(request, 'inventario/confirmar_eliminar.html', {'material': material})


# inventario/views.py


@login_required
def registrar_acta(request):
        # 🔒 Solo técnicos pueden acceder
    if request.user.groups.first().name != 'tecnico':
        return HttpResponseForbidden("Solo técnicos pueden registrar actas.")

    acta = ActaEntrega.objects.filter(tecnico=request.user, firmada_por_tecnico=False).first()
    if not acta:
        acta = ActaEntrega.objects.create(tecnico=request.user)

    materiales = Material.objects.filter(activo=True).order_by('descripcion')

    if request.method == 'POST':
        material_codigo = request.POST.get('material')
        cantidad = request.POST.get('cantidad')

        # Validar material por código
        try:
            material = Material.objects.get(codigo=material_codigo)
        except Material.DoesNotExist:
            messages.error(request, "⚠️ El código ingresado no corresponde a ningún material.")
            return redirect('inventario:registrar_acta')

        # Validar cantidad
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError
        except (TypeError, ValueError):
            messages.error(request, "⚠️ Debes ingresar una cantidad válida.")
            return redirect('inventario:registrar_acta')

        # Registrar ítem
        DetalleEntrega.objects.create(
            acta=acta,
            material=material,
            cantidad=cantidad,
            reparado_por=request.user
        )
        messages.success(request, "✅ Material agregado.")
        return redirect('inventario:registrar_acta')

    detalles = acta.detalles.select_related('material').all()
    return render(request, 'inventario/acta_base.html', {
        'acta': acta,
        'materiales': materiales,
        'detalles': detalles, 
        'modo_lectura': False,
    })




@login_required
def detalle_acta(request, pk):
    acta = get_object_or_404(ActaEntrega, pk=pk)
    materiales = Material.objects.filter(activo=True).order_by('descripcion')
    detalles = acta.detalles.select_related('material', 'reparado_por')
    tiene_aprobaciones = Aprobacion.objects.filter(
    content_type=ContentType.objects.get_for_model(acta),
    object_id=acta.id
    ).exists()



    tipo_aprobador = obtener_etapa_usuario(request.user)
    etapa_actual = obtener_etapa_pendiente(acta)
    puede_editar = request.user == acta.tecnico and not acta.firmada_por_tecnico
    puede_aprobar = tipo_aprobador == etapa_actual and etapa_actual is not None

    if tipo_aprobador in FLUJO_ETAPAS and acta.firmada_por_tecnico and detalles.exists():
        puede_aprobar = True
        content_type = ContentType.objects.get_for_model(acta)
        for etapa in etapas_previas(tipo_aprobador):
            if not Aprobacion.objects.filter(
                tipo=etapa,
                content_type=content_type,
                object_id=acta.id,
                estado='aprobado'
            ).exists():
                puede_aprobar = False
                break

    # 👇 Lógica para agregar materiales a la acta
        if request.method == 'POST' and puede_editar:

            
            codigo = request.POST.get('material')
            cantidad = request.POST.get('cantidad')

            try:
                material = Material.objects.get(codigo=codigo)
            except Material.DoesNotExist:
                messages.error(request, "⚠️ El código ingresado no corresponde a ningún material.")
                return redirect('inventario:detalle_acta', pk=pk)

            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    raise ValueError
            except (TypeError, ValueError):
                messages.error(request, "⚠️ Debes ingresar una cantidad válida.")
                return redirect('inventario:detalle_acta', pk=pk)

            DetalleEntrega.objects.create(
                acta=acta,
                material=material,
                cantidad=cantidad,
                reparado_por=request.user
            )
            messages.success(request, "✅ Material agregado a la acta.")
            return redirect('inventario:detalle_acta', pk=pk)

    return render(request, "inventario/acta_base.html", {
        "acta": acta,
        "detalles": detalles,
        "materiales": materiales,
        "tipo_aprobador": tipo_aprobador,
        "etapas": FLUJO_ETAPAS,
        "puede_editar": puede_editar,
        "puede_aprobar": puede_aprobar,
        "etapa_actual": etapa_actual,
        "aprobaciones": obtener_dict_aprobaciones(acta),
        "tiene_aprobaciones": tiene_aprobaciones,
    })

    



@login_required
def agregar_detalle(request, pk):
    """Recibe el POST del formulario y guarda la línea como en una caja registradora"""

    acta = get_object_or_404(ActaEntrega, pk=pk)

    grupo = request.user.groups.first().name.lower() if request.user.groups.exists() else ''
    if acta.firmada_por_tecnico or (request.user != acta.tecnico and grupo != 'supervisor'):
        return HttpResponseForbidden("Solo el técnico responsable o un supervisor pueden modificar esta acta sin firmar.")

    if request.method == 'POST':
        material_id = request.POST.get('material')
        cantidad = request.POST.get('cantidad')

        if not material_id or not cantidad:
            messages.error(request, "Debes seleccionar material y cantidad.")
            return redirect('inventario:detalle_acta', pk=pk)

        DetalleEntrega.objects.create(
            acta=acta,
            material_id=material_id,
            cantidad=cantidad,
            reparado_por=request.user,  # Puede ser técnico o supervisor
        )
        messages.success(request, "✅ Material agregado.")
        return redirect('inventario:detalle_acta', pk=pk)

    return redirect('inventario:detalle_acta', pk=pk)


@login_required
def eliminar_item_acta(request, item_id):
    try:
        item = DetalleEntrega.objects.select_related('acta').get(id=item_id)
    except DetalleEntrega.DoesNotExist:
        messages.error(request, "⚠️ El ítem no existe.")
        return redirect('inventario:lista_actas')  # o algún fallback seguro

    acta = item.acta

    # 🔒 Validaciones de permiso
    if acta.tecnico != request.user:
        messages.error(request, "⛔ No tienes permiso para modificar esta acta.")
        return redirect('inventario:detalle_acta', pk=acta.id)

    if acta.firmada_por_tecnico:
        messages.warning(request, "🔒 Esta acta ya fue firmada y no se puede modificar.")
        return redirect('inventario:detalle_acta', pk=acta.id)

    if request.method == 'POST':
        item.delete()
        messages.success(request, "🗑️ Material eliminado del acta.")
        return redirect('inventario:detalle_acta', pk=acta.id)

    return render(request, 'inventario/confirmar_eliminar_item.html', {'item': item, 'acta': acta})




@login_required
def firmar_acta(request, pk):
    acta = get_object_or_404(ActaEntrega, pk=pk, tecnico=request.user)

    if acta.firmada_por_tecnico:
        messages.info(request, f"ℹ️ El acta #{pk} ya estaba firmada.")
        return redirect('inventario:detalle_acta', pk=pk)

    if not acta.detalles.exists():
        messages.warning(request, "❌ No puedes firmar un acta sin materiales.")
        return redirect('inventario:detalle_acta', pk=pk)

    # Marcar como firmada
    acta.firmada_por_tecnico = True
    acta.save()

    # Registrar la "aprobación técnica"
    content_type = ContentType.objects.get_for_model(acta)
    Aprobacion.objects.update_or_create(
        content_type=content_type,
        object_id=acta.id,
        tipo='tecnico',
        defaults={
            'estado': 'aprobado',
            'comentario': 'Acta completada por el técnico.',
            'usuario': request.user,
        }
    )
    messages.success(request, f"✅ Acta #{pk} firmada exitosamente.")
    messages.info(request, "📤 Ahora está pendiente de aprobación por el supervisor.")
    return redirect('inventario:detalle_acta', pk=pk)


@login_required
def lista_actas(request):
    actas = ActaEntrega.objects.select_related('tecnico').prefetch_related('detalles', 'detalles__material').order_by('-id')

    tecnico_id = request.GET.get('tecnico')
    estado_filtro = request.GET.get('estado')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')

    if tecnico_id:
        actas = actas.filter(tecnico_id=tecnico_id)

    if fecha_desde:
        actas = actas.filter(fecha__gte=parse_date(fecha_desde))
    if fecha_hasta:
        actas = actas.filter(fecha__lte=parse_date(fecha_hasta))

    # Calculamos y anotamos estado_actual
    actas_list = list(actas)  # convertimos queryset para poder iterar y modificar
    for acta in actas_list:
        acta.estado_actual = obtener_estado_acta(acta)

    # Filtrado por estado dinámico
    if estado_filtro:
        actas_list = [a for a in actas_list if a.estado_actual == estado_filtro]

    tecnico_ids = [a.tecnico_id for a in actas_list]
    tecnicos = User.objects.filter(id__in=tecnico_ids)

    return render(request, 'inventario/acta_listado.html', {
        'actas': actas_list,
        'tecnicos': tecnicos,
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'estado': estado_filtro,  # para mantener seleccionado el filtro
    })




def obtener_estado_acta(acta):
    if not acta.firmada_por_tecnico:
        return 'pendiente'

    content_type = ContentType.objects.get_for_model(acta)
    aprobaciones = {
        a.tipo: a.estado for a in Aprobacion.objects.filter(content_type=content_type, object_id=acta.id)
    }

    if 'rechazado' in aprobaciones.values():
        return 'rechazada'
    elif all(aprobaciones.get(k) == 'aprobado' for k in ['tecnico', 'supervisor', 'seguridad', 'almacen']):
        return 'aprobada'
    return 'en_aprobacion'

# inventario/views.py
from django.http import HttpResponse
from django.db.models import Count, Sum
from .models import ActaEntrega, DetalleEntrega
from collections import defaultdict

def dashboard_actas(request):
    # Filtramos actas válidas
    actas = ActaEntrega.objects.exclude(fecha__isnull=True)

    # Agrupamos manualmente por mes y año
    resumen_por_mes = defaultdict(int)
    for acta in actas:
        clave = acta.fecha.strftime('%b %Y')  # Ej: 'Abr 2025'
        resumen_por_mes[clave] += 1

    entregas_labels = list(resumen_por_mes.keys())
    entregas_data = list(resumen_por_mes.values())

    materiales_top = (
        DetalleEntrega.objects
        .values('material__codigo', 'material__descripcion')
        .annotate(cantidad_total=Sum('cantidad'))
        .order_by('-cantidad_total')[:10]
    )

    tecnicos_top = (
        ActaEntrega.objects
        .values('tecnico__username')
        .annotate(total=Count('id'))
        .order_by('-total')[:5]
    )

    context = {
        'entregas_labels': entregas_labels,
        'entregas_data': entregas_data,
        'materiales_top': materiales_top,
        'tecnicos_top': tecnicos_top,
    }
    return render(request, 'inventario/dashboard_actas.html', context)