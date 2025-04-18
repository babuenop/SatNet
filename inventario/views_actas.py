import os
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from weasyprint import HTML
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from .models import ActaEntrega
from aprobaciones.models import Aprobacion

def acta_pdf(request, acta_id):
    acta = get_object_or_404(ActaEntrega, pk=acta_id)
    detalles = acta.detalles.select_related('material', 'reparado_por')

    # Obtener aprobaciones por etapa
    content_type = ContentType.objects.get_for_model(acta)
    aprobaciones_qs = Aprobacion.objects.filter(content_type=content_type, object_id=acta.id)
    aprobaciones = {a.tipo: a for a in aprobaciones_qs}
    # Definir las etapas
    etapas = ['tecnico', 'supervisor', 'seguridad', 'almacen']


    # Ruta absoluta para el logo
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'logo.jpg')
    logo_url = f'file://{logo_path}'

    html_string = render_to_string('actas/acta_pdf.html', {
        'acta': acta,
        'detalles': detalles,
        'logo_url': logo_url,
        'aprobaciones': aprobaciones,
        'etapas': etapas,  # 👈 aquí
    })


    pdf = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=Acta_{acta.id}.pdf'
    return response
