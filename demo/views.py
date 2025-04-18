from django.shortcuts import render, get_object_or_404
from .models import DocumentoDemo
from aprobaciones.models import Aprobacion
from django.contrib.contenttypes.models import ContentType

def detalle_demo(request, pk):
    doc = get_object_or_404(DocumentoDemo, pk=pk)
    content_type = ContentType.objects.get_for_model(doc)
    aprobaciones = {
        a.tipo: a for a in Aprobacion.objects.filter(content_type=content_type, object_id=doc.id)
    }
    return render(request, 'demo/detalle_demo.html', {
        'documento': doc,
        'aprobaciones': aprobaciones,
    })

# Create your views here.
