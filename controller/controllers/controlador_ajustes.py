from controller.controlador_principal import ControladorPrincipal

from view.views.vista_ubicacion import VistaUbicacion
from controller.controllers.controlador_ubicacion import ControladorUbicacion

class ControladorAjustes(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def ir_a_ubicacion(self):
        controlador_ubicacion = ControladorUbicacion(self.app)
        vista_ubicacion = VistaUbicacion(self.app, controlador_ubicacion)
        self.app.cambiar_frame(vista_ubicacion)

    def regresar(self):
        self.app.volver_frame_anterior()