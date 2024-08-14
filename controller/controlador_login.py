import datetime
import secrets
import bcrypt

from model.usuario import Usuario
from auth.sesion import Sesion


class ControladorLogin():
    def __init__(self, app):
        self.app = app

    # Publicos

    def crear_sesion(self, nombre_usuario):
        usuario = Usuario.obtener_usuario_nombre_usuario(self.app.cliente, nombre_usuario)
        Sesion.crear_sesion(self.app.cliente, usuario)

    def autenticar_usuario(self, nombre_usuario, contrasena):
        if not self._validar_campos(nombre_usuario, contrasena):
            self._generar_evento_campos_vacios()
            return False
        usuario = Usuario.obtener_usuario_nombre_usuario(self.app.cliente, nombre_usuario)
        if not usuario or not usuario.validar_credenciales(contrasena):
            self._generar_evento_datos_invalidos()
            return False
        return True

    def registrar_usuario(self, nombre_usuario, contrasena):
        if not self._validar_campos(nombre_usuario, contrasena):
            self._generar_evento_campos_vacios()
            return False
        # Aqui podria implementar Usuario.existe_usuario()
        if Usuario.obtener_usuario_nombre_usuario(self.app.cliente, nombre_usuario) is not None:
            self._generar_evento_usuario_en_uso()
            return False
        Usuario.crear_usuario(self.app.cliente, nombre_usuario, contrasena)
        return True

    def ir_a_inicio(self):
        self.app.ir_a_inicio()

    # Privados

    def _validar_campos(self, nombre_usuario, contrasena):
        return bool(nombre_usuario and contrasena)

    def _generar_evento_campos_vacios(self):
        self.app.event_generate("<<campos_vacios>>")

    def _generar_evento_datos_invalidos(self):
        self.app.event_generate("<<datos_invalidos>>")

    def _generar_evento_usuario_en_uso(self):
        self.app.event_generate("<<en_uso>>")
