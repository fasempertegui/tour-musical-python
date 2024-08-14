import datetime
import os


class SesionBD:
    @staticmethod
    def validar_sesion(cliente, id_sesion):
        sesion = cliente[os.getenv("BD_SESIONES")].find_one({"_id": id_sesion})
        return sesion and sesion["expiracion"] > datetime.datetime.utcnow()

    @staticmethod
    def guardar_sesion(cliente, sesion):
        cliente[os.getenv("BD_SESIONES")].insert_one(sesion)

    @staticmethod
    def eliminar_sesion(cliente, id_sesion):
        cliente[os.getenv("BD_SESIONES")].delete_one({"_id": id_sesion})
