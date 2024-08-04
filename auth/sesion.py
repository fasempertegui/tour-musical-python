import os
import secrets
import datetime

from model.usuario import Usuario
from auth.token import Token


class Sesion:

    @classmethod
    def crear_sesion(cls, cliente, id_usuario):
        token = secrets.token_hex(16)
        expiracion = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        sesion = {
            "token": token,
            "id_usuario": id_usuario,
            "expiracion": expiracion
        }
        bd_sesiones = os.getenv("BD_SESIONES")
        cliente[bd_sesiones].insert_one(sesion)
        Token.guardar_token(token)
        return True

    @classmethod
    def validar_sesion(cls, cliente):
        token = Token.obtener_token()
        if not token:
            return False
        bd_sesiones = os.getenv("BD_SESIONES")
        sesion = cliente[bd_sesiones].find_one({"token": token})
        return sesion and sesion["expiracion"] > datetime.datetime.utcnow()

    @classmethod
    def eliminar_sesion(cls, cliente):
        token = Token.obtener_token()
        if token:
            bd_sesiones = os.getenv("BD_SESIONES")
            cliente[bd_sesiones].delete_one({"token": token})
            Token.eliminar_token()

    @classmethod
    def obtener_usuario_actual(cls, cliente):
        sesion = cls._obtener_sesion(cliente)
        usuario_actual = Usuario.obtener_usuario_id(cliente, sesion["id_usuario"])
        return usuario_actual

    @classmethod
    def actualizar_eventos_asistidos(cls, cliente, id_evento):
        usuario_actual = cls.obtener_usuario_actual(cliente)
        if usuario_actual:
            Usuario.actualizar_eventos(cliente, usuario_actual._id, id_evento)

    @classmethod
    def actualizar_configuracion_ubicacion(cls, cliente, coordenadas):
        usuario_actual = cls.obtener_usuario_actual(cliente)
        if usuario_actual:
            Usuario.actualizar_configuracion(cliente, usuario_actual._id, coordenadas)

    @classmethod
    def _obtener_sesion(cls, cliente):
        token = Token.obtener_token()
        if token:
            bd_sesiones = os.getenv("BD_SESIONES")
            sesion = cliente[bd_sesiones].find_one({"token": token})
            if sesion and sesion["expiracion"] > datetime.datetime.utcnow():
                return sesion
        return None
