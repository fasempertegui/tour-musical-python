from functools import wraps
from utils.utils_sesion import SesionUtils


def requiere_sesion_valida(func):
    @wraps(func)
    def wrapper(instancia, *args, **kwargs):
        if SesionUtils.validar_sesion(instancia.app.cliente):
            return func(instancia, *args, **kwargs)
        else:
            print("Sesión inválida o no existe. Redirigiendo al login.")
            instancia.app.ir_a_login()
            return None
    return wrapper
