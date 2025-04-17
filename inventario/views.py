from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ActaEntrega, DetalleEntrega, Material
from .forms import MaterialForm



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

from django.contrib import messages
from django.shortcuts import get_object_or_404

@login_required
def registrar_acta(request):
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
    acta = get_object_or_404(ActaEntrega, pk=pk, tecnico=request.user)
    materiales = Material.objects.filter(activo=True).order_by('descripcion')

    if request.method == 'POST':
        codigo = request.POST.get('material')
        cantidad = request.POST.get('cantidad')

        # Validar que exista el código de material
        try:
            material = Material.objects.get(codigo=codigo)
        except Material.DoesNotExist:
            messages.error(request, "⚠️ El código ingresado no corresponde a ningún material.")
            return redirect('inventario:detalle_acta', pk=pk)

        # Validar cantidad
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError
        except (TypeError, ValueError):
            messages.error(request, "⚠️ Debes ingresar una cantidad válida.")
            return redirect('inventario:detalle_acta', pk=pk)

        # Crear ítem
        DetalleEntrega.objects.create(
            acta=acta,
            material=material,
            cantidad=cantidad,
            reparado_por=request.user
        )
        messages.success(request, "✅ Material agregado a la acta.")
        return redirect('inventario:detalle_acta', pk=pk)

    # GET: mostrar formulario
    detalles = acta.detalles.select_related('material', 'reparado_por')

    return render(request, 'inventario/acta_base.html', {
        'acta': acta,
        'materiales': materiales,
        'detalles': detalles,
        'modo_lectura': False,
    })




@login_required
def agregar_detalle(request, pk):
    """Recibe el POST del formulario y guarda la línea como en una caja registradora"""
    acta = get_object_or_404(
        ActaEntrega,
        pk=pk,
        tecnico=request.user,
        firmada_por_tecnico=False,
    )

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
            reparado_por=request.user,
        )

    return redirect('inventario:detalle_acta', pk=pk)


@login_required
def firmar_acta(request, pk):
    acta = get_object_or_404(ActaEntrega, pk=pk, tecnico=request.user)

    if acta.firmada_por_tecnico:
        messages.info(request, f"ℹ️ El acta #{pk} ya estaba firmada.")
        return redirect('inventario:detalle_acta', pk=pk)

    if not acta.detalles.exists():
        messages.warning(request, "❌ No puedes firmar un acta sin materiales.")
        return redirect('inventario:detalle_acta', pk=pk)

    acta.firmada_por_tecnico = True
    acta.save()

    messages.success(request, f"✅ Acta #{pk} firmada exitosamente.")
    return redirect('inventario:lista_actas')



@login_required
def lista_actas(request):
    actas = ActaEntrega.objects.order_by('-id')
    return render(request, 'inventario/acta_listado.html', {'actas': actas})


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
