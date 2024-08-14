import os
import secrets

from auth.sesion_BD import SesionBD
from auth.sesion_local import SesionLocal


class Sesion:
    def __init__(self, _id, id_usuario, expiracion):
        self._id = _id
        self.id_usuario = id_usuario
        self.expiracion = expiracion

    # Metodos de clase

    @classmethod
    def obtener_sesion(cls, cliente):
        if SesionLocal.existe_sesion_local():
            id_sesion = SesionLocal.obtener_id_sesion_local()
            sesion = cliente[os.getenv("BD_SESIONES")].find_one({"_id": id_sesion})
            if sesion:
                return cls(**sesion)
        return None

    # Metodos estaticos

    @staticmethod
    def crear_sesion(cliente, usuario):
        id_sesion = secrets.token_hex(16)
        SesionLocal.guardar_id_sesion_local(id_sesion)
        SesionBD.guardar_sesion(cliente, id_sesion, usuario._id)

    @staticmethod
    def eliminar_sesion(cliente, id_sesion):
        SesionLocal.eliminar_sesion_local()
        SesionBD.eliminar_sesion(cliente, id_sesion)

    @staticmethod
    def validar_sesion(cliente):
        if SesionLocal.existe_sesion_local():
            id_sesion = SesionLocal.obtener_id_sesion_local()
            if SesionBD.validar_sesion(cliente, id_sesion):
                return True
        return False
