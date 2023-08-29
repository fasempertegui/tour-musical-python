from controller.controlador_principal import ControladorPrincipal
from model.usuario import Sesion

class ControladorLogin(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def autenticar(self, nombre_usuario, contrasena):
        if nombre_usuario != '' and contrasena != '':
            if Sesion.autenticar(nombre_usuario, contrasena):
                return True
            else:
                self.app.event_generate("<<DatosInvalidos>>")
                return False
        else:
            self.app.event_generate("<<CamposVacios>>")
            return False

    def registrar(self, nombre_usuario, contrasena):
        if nombre_usuario != '' and contrasena != '':
            if Sesion.registrar(self.app.cliente, nombre_usuario, contrasena):
                return True
            else:
                self.app.event_generate("<<EnUso>>")
                return False
        else:
            self.app.event_generate("<<CamposVacios>>")
        return False

    def renderizar(self):
        self.app.event_generate("<<Login>>")