from controller.controlador_principal import ControladorPrincipal

from model.usuario import Usuario
from auth.sesion import Sesion

from view.views.vista_inicio import VistaInicio
from controller.controllers.controlador_inicio import ControladorInicio


class ControladorLogin(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def autenticar_usuario(self, nombre_usuario, contrasena):
        if not self._validar_campos(nombre_usuario, contrasena):
            self.app.event_generate("<<campos_vacios>>")
            return False
        usuario = self._obtener_usuario(nombre_usuario)
        if not usuario or not self._validar_credenciales(usuario, contrasena):
            self.app.event_generate("<<datos_invalidos>>")
            return False
        self._iniciar_sesion(usuario)
        return True

    def registrar_usuario(self, nombre_usuario, contrasena):
        if not self._validar_campos(nombre_usuario, contrasena):
            self.app.event_generate("<<campos_vacios>>")
            return False
        if self._obtener_usuario(nombre_usuario) is not None:
            self.app.event_generate("<<en_uso>>")
            return False
        nuevo_usuario = self._crear_usuario(nombre_usuario, contrasena)
        return self._iniciar_sesion(nuevo_usuario)

    def _validar_campos(self, nombre_usuario, contrasena):
        return nombre_usuario and contrasena

    def _obtener_usuario(self, nombre_usuario):
        return Usuario.obtener_usuario_nombre_usuario(self.app.cliente, nombre_usuario)

    def _validar_credenciales(self, usuario, contrasena):
        return usuario.validar_credenciales(contrasena)

    def _iniciar_sesion(self, usuario):
        return Sesion.crear_sesion(self.app.cliente, usuario._id)

    def _crear_usuario(self, nombre_usuario, contrasena):
        return Usuario.crear_usuario(self.app.cliente, nombre_usuario, contrasena)

    def ir_a_inicio(self):
        self.app.historial_vistas = []
        controlador_inicio = ControladorInicio(self.app)
        vista_inicio = VistaInicio(self.app, controlador_inicio)
        self.app.cambiar_frame(vista_inicio)
