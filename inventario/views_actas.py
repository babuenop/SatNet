import os
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from weasyprint import HTML
from django.conf import settings

from .models import ActaEntrega

def acta_pdf(request, acta_id):
    acta = get_object_or_404(ActaEntrega, pk=acta_id)
    detalles = acta.detalles.all()


    # Ruta absoluta para el logo

    logo_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'logo.jpg')
    logo_url = f'file://{logo_path}'  # ✅ importante el "file://"

    html_string = render_to_string('actas/acta_pdf.html', {
        'acta': acta,
        'detalles': detalles,
        'logo_url': logo_url  # se pasa al template
    })

    
    pdf = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=Acta_{acta.id}.pdf'
    return response
