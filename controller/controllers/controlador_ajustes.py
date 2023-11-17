from controller.controlador_principal import ControladorPrincipal

from model.usuario import Sesion

class ControladorAjustes(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def establecer_ubicacion(self, coordenadas):
        Sesion.actualizar_configuracion_ubicacion(self.app.cliente, coordenadas)

    def regresar(self):
        self.app.volver_frame_anterior()