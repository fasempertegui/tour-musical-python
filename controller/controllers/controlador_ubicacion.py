from controller.controlador_principal import ControladorPrincipal

from model.usuario import Sesion

class ControladorUbicacion(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def guardar_cambios(self, coordenadas, *args):
        Sesion.actualizar_configuracion_ubicacion(self.app.cliente, coordenadas)

    def regresar(self):
        self.app.volver_frame_anterior()