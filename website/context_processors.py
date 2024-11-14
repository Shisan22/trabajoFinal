# myapp/context_processors.py
from .views import is_chef

def chef_status(request):
    # Devuelve un diccionario con el valor de is_chef para el usuario autenticado
    return {'is_chef': is_chef(request.user)}