import datetime
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
    def obtener_sesion_id(cls, cliente, id_sesion):
        sesion = cliente[os.getenv("BD_SESIONES")].find_one({"_id": id_sesion})
        return cls(**sesion) if sesion else None

    # Metodos estaticos

    @staticmethod
    def crear_sesion(cliente, usuario):
        id_sesion = secrets.token_hex(16)
        sesion = {
            "_id": id_sesion,
            "id_usuario": usuario._id,
            "expiracion": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        SesionLocal.guardar_sesion_local(sesion["_id"])
        SesionBD.guardar_sesion(cliente, sesion)

    @staticmethod
    def eliminar_sesion(cliente, id_sesion):
        SesionLocal.eliminar_sesion_local()
        SesionBD.eliminar_sesion(cliente, id_sesion)

    @staticmethod
    def existe_sesion_local():
        return SesionLocal.existe_sesion_local()

    @staticmethod
    def obtener_sesion_local():
        return SesionLocal.obtener_sesion_local()

    @staticmethod
    def validar_sesion(cliente, id_sesion):
        return SesionBD.validar_sesion(cliente, id_sesion)
