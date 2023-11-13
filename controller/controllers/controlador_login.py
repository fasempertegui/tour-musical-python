from controller.controlador_principal import ControladorPrincipal
from model.usuario import Usuario, Sesion


class ControladorLogin(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def autenticar(self, nombre_usuario, contrasena):
        if nombre_usuario == '' or contrasena == '':
            self.app.event_generate("<<CamposVacios>>")
            return False
        if not Sesion.autenticar(nombre_usuario, contrasena):
            self.app.event_generate("<<DatosInvalidos>>")
            return False
        return True

    def registrar(self, nombre_usuario, contrasena):
        if nombre_usuario == '' or contrasena == '':
            self.app.event_generate("<<CamposVacios>>")
            return False
        if not Usuario.nombre_usuario_disponible(nombre_usuario):
            self.app.event_generate("<<EnUso>>")
            return False
        Sesion.registrar(self.app.cliente, nombre_usuario, contrasena)
        return True

    def renderizar(self):
        self.app.event_generate("<<Login>>")
