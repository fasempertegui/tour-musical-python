from auth.sesion import Sesion
from model.usuario import Usuario


class SesionUtils():

    @staticmethod
    def obtener_usuario_sesion(cliente):
        sesion = Sesion.obtener_sesion(cliente)
        if sesion:
            usuario = Usuario.obtener_usuario_id(cliente, sesion.id_usuario)
            if usuario:
                return usuario
        return None
