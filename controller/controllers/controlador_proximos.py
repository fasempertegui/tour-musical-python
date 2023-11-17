from controller.controlador_principal import ControladorPrincipal

from view.views.vista_mapa import VistaMapa
from controller.controllers.controlador_mapa import ControladorMapa


class ControladorProximos(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    # Navegacion

    def ir_a_mapa(self):
        controlador_mapa = ControladorMapa(self.app)
        vista_mapa = VistaMapa(self.app, controlador_mapa)
        self.app.cambiar_frame(vista_mapa)
        self.app.event_generate("<<Mapa>>")

    def regresar(self):
        self.app.volver_frame_anterior()
