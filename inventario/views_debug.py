from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def cambiar_usuario(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        # ✅ MUY IMPORTANTE: guardar el admin_id antes del login
        if request.user.is_superuser and 'admin_id' not in request.session:
            request.session['admin_id'] = request.user.id
            print(f"✅ admin_id guardado en sesión: {request.user.id}")

        # ⛔ login DEBE venir DESPUÉS de guardar el admin_id
        login(request, user)
        print(f"🎭 Login como: {user.username} (ID: {user.id})")

        # ✅ Limpiar si estamos volviendo al admin original
        if 'admin_id' in request.session and user.id == request.session['admin_id']:
            del request.session['admin_id']
            print(f"🧹 admin_id eliminado, volviste al admin.")

        messages.success(request, f"Sesión cambiada a {user.username}")

    except User.DoesNotExist:
        messages.error(request, "Usuario no encontrado.")
        print("❌ Usuario destino no existe.")

    return redirect(request.META.get('HTTP_REFERER', '/'))
