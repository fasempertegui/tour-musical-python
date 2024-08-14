import datetime
import os


class SesionBD:
    @staticmethod
    def validar_sesion(cliente, id_sesion):
        sesion = cliente[os.getenv("BD_SESIONES")].find_one({"_id": id_sesion})
        return sesion and sesion["expiracion"] > datetime.datetime.utcnow()

    @staticmethod
    def guardar_sesion(cliente, id_sesion, id_usuario):
        sesion = {
            "_id": id_sesion,
            "id_usuario": id_usuario,
            "expiracion": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        cliente[os.getenv("BD_SESIONES")].insert_one(sesion)

    @staticmethod
    def eliminar_sesion(cliente, id_sesion):
        cliente[os.getenv("BD_SESIONES")].delete_one({"_id": id_sesion})
