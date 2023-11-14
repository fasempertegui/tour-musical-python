from controller.controlador_principal import ControladorPrincipal
from model.usuario import Sesion


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

    def renderizar(self):
        self.app.event_generate("<<Login>>")
