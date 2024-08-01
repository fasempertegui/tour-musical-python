from controller.controlador_principal import ControladorPrincipal

from model.sesion import Sesion

class ControladorUbicacion(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def establecer_coordenadas(self, coordenadas):
        self.coordenadas = coordenadas

    def guardar_cambios(self, *args):
        Sesion.actualizar_configuracion_ubicacion(self.app.cliente, self.coordenadas)

    def regresar(self):
        self.app.volver_frame_anterior()