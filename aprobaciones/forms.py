# aprobaciones/forms.py
from django import forms

class ComentarioAprobacionForm(forms.Form):
    comentario = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label="Comentario")
