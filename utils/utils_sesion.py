from auth.sesion import Sesion
from model.usuario import Usuario


class SesionUtils():

    @staticmethod
    def validar_sesion(cliente):
        if Sesion.existe_sesion_local():
            id_sesion = Sesion.obtener_sesion_local()
            if Sesion.validar_sesion(cliente, id_sesion):
                return True
            Sesion.eliminar_sesion(cliente, id_sesion)
        return False

    @staticmethod
    def obtener_usuario_sesion(cliente):
        id_sesion = Sesion.obtener_sesion_local()
        sesion = Sesion.obtener_sesion_id(cliente, id_sesion)
        usuario = Usuario.obtener_usuario_id(cliente, sesion.id_usuario)
        return usuario
