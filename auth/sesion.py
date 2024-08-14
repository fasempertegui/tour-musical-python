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
        id_sesion = cls._obtener_id_sesion_local()
        if id_sesion:
            sesion = cliente[os.getenv("BD_SESIONES")].find_one({"_id": id_sesion})
            if sesion:
                return cls(**sesion)
        return None

    @classmethod
    def validar_sesion(cls, cliente):
        id_sesion = cls._obtener_id_sesion_local()
        if id_sesion:
            return SesionBD.validar_sesion(cliente, id_sesion)
        return False

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

    # Metodos privados

    @staticmethod
    def _obtener_id_sesion_local():
        if SesionLocal.existe_sesion_local():
            return SesionLocal.obtener_id_sesion_local()
        return None
