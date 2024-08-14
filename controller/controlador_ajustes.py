from view.views.vista_ubicacion import VistaUbicacion
from controller.controlador_ubicacion import ControladorUbicacion


class ControladorAjustes():
    def __init__(self, app):
        self.app = app

    def ir_a_ubicacion(self):
        self.app.cambiar_vista(ControladorUbicacion, VistaUbicacion)

    def regresar(self):
        self.app.volver_vista_anterior()
