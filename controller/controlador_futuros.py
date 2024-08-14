from controller.controlador_eventos import ControladorEventos
from controller.controlador_mapa import ControladorMapa
from view.vista_mapa import VistaMapa


class ControladorFuturos(ControladorEventos):

    def __init__(self, app, evento=None, ubicacion=None):
        super().__init__(app)
        self.evento = evento
        self.ubicacion = ubicacion

    def obtener_evento_actual(self):
        return self.evento

    def obtener_ubicacion_actual(self):
        return self.ubicacion

    # Navegacion

    def ir_a_mapa(self):
        self.app.cambiar_vista(ControladorMapa, VistaMapa, self.ubicacion)
