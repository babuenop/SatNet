from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static


# Redirección raíz: si querés llevar al usuario al inventario directamente
def home(request):
    return redirect('inventario:lista_materiales')

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    

    # Módulo principal
    path('inventario/', include('inventario.urls')),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # Aprobaciones
    path('aprobaciones/', include('aprobaciones.urls')),
    path('', include('demo.urls')),
    
    # Ruta raíz
    path('', home),  # redirige a lista de materiales (u otra vista central)

]

# Sirve archivos estáticos solo si estás en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
