# aprobaciones/decorators.py
from django.http import HttpResponseForbidden
from functools import wraps

def require_aprobador(tipo):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.groups.filter(name=tipo).exists():
                return HttpResponseForbidden("No tienes permisos para realizar esta aprobación.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
