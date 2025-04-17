from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'inventario'

urlpatterns = [
    
 # ---------- Materiales ----------
    path("", views.lista_materiales, name="lista_materiales"),
    path("nuevo/", views.crear_material, name="crear_material"),
    path("<int:pk>/editar/", views.editar_material, name="editar_material"),
    path("<int:pk>/eliminar/", views.eliminar_material, name="eliminar_material"),

    # ---------- Flujo POS de actas ----------
    path('actas/registrar/', views.registrar_acta, name='registrar_acta'),
    path("actas/<int:pk>/detalles/", views.detalle_acta, name="detalle_acta"),
    path("actas/<int:pk>/detalles/agregar/", views.agregar_detalle, name="agregar_detalle"),
    path("actas/<int:pk>/firmar/", views.firmar_acta, name="firmar_acta"),
    path("actas/", views.lista_actas, name="lista_actas"),

    # ---------- Autenticación ----------
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="inventario:login"), name="logout"),

 
]
