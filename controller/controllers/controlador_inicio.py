from controller.controlador_principal import ControladorPrincipal
from model.usuario import Sesion

class ControladorInicio(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def cerrar_sesion(self):
        self.app.event_generate("<<Logout>>")
        Sesion.cerrar_sesion()

    def ir_a_ajustes(self):
        self.app.cambiar_frame(self.app.vista_ajustes)

    def ir_a_explorar(self):
        self.app.cambiar_frame(self.app.vista_explorar)

    def ir_a_busqueda(self):
        self.app.cambiar_frame(self.app.vista_busqueda)

    def ir_a_asistidos(self):
        self.app.cambiar_frame(self.app.vista_asistidos)