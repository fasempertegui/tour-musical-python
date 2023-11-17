from controller.controlador_principal import ControladorPrincipal
from model.usuario import Sesion

from view.views.vista_inicio import VistaInicio
from controller.controllers.controlador_inicio import ControladorInicio


class ControladorLogin(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def autenticar_usuario(self, nombre_usuario, contrasena):
        cliente = self.app.cliente
        if nombre_usuario == '' or contrasena == '':
            self.app.event_generate("<<CamposVacios>>")
            return False
        if not Sesion.autenticar_usuario(cliente, nombre_usuario, contrasena):
            self.app.event_generate("<<DatosInvalidos>>")
            return False
        return True

    def registrar_usuario(self, nombre_usuario, contrasena):
        cliente = self.app.cliente
        if nombre_usuario == '' or contrasena == '':
            self.app.event_generate("<<CamposVacios>>")
            return False
        if self.obtener_usuario_nombre_usuario(nombre_usuario) is not None:
            self.app.event_generate("<<EnUso>>")
            return False
        Sesion.registrar_usuario(cliente, nombre_usuario, contrasena)
        return True

    def ir_a_inicio(self):
        self.app.historial_vistas = []
        controlador_inicio = ControladorInicio(self.app)
        vista_inicio = VistaInicio(self.app, controlador_inicio)
        self.app.cambiar_frame(vista_inicio)
