from functools import wraps
from auth.sesion import Sesion


def requiere_sesion_valida(func):
    @wraps(func)
    def wrapper(instancia, *args, **kwargs):
        if Sesion.validar_sesion(instancia.app.cliente):
            return func(instancia, *args, **kwargs)
        else:
            print("Sesión inválida o no existe. Redirigiendo al login.")
            instancia.app.ir_a_login()
            return None
    return wrapper
