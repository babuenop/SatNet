from django.urls import path
from . import views

app_name = 'aprobaciones'

urlpatterns = [
    path('pendientes/', views.mis_aprobaciones, name='mis_aprobaciones'),
    path('<str:tipo>/<str:app_label>/<str:model>/<int:object_id>/aprobar/', views.aprobar_objeto, name='aprobar'),
    path('<str:tipo>/<str:app_label>/<str:model>/<int:object_id>/rechazar/', views.rechazar_objeto, name='rechazar'),
    
]
