# inventario/forms.py
from django import forms
from django.forms.models import inlineformset_factory
from .models import Material, ActaEntrega, DetalleEntrega

# ---------- FORMULARIO DE MATERIALES ----------
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['codigo', 'descripcion', 'proveedor', 'estado', 'stock', 'unidad']

# ---------- FORMULARIO DE ACTA ----------
class ActaEntregaForm(forms.ModelForm):
    class Meta:
        model = ActaEntrega
        exclude = ['tecnico', 'cerrada_por_tecnico', 'fecha']


# ---------- FORMULARIO DE DETALLE ----------
class DetalleEntregaForm(forms.ModelForm):
    class Meta:
        model = DetalleEntrega
        fields = ['material', 'cantidad', 'reparado_por']



# ---------- FORMSET de DETALLES ----------
DetalleEntregaFormSet = inlineformset_factory(
    ActaEntrega,
    DetalleEntrega,
    form=DetalleEntregaForm,
    extra=1,
    can_delete=True
)
