from django.urls import path
from .views import detalle_demo

urlpatterns = [
    path('demo/<int:pk>/', detalle_demo, name='detalle_demo'),
]
