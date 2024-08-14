from controller.controlador_eventos import ControladorEventos

from model.evento import Evento


class ControladorBusqueda(ControladorEventos):

    def __init__(self, app):
        super().__init__(app)
        self.eventos_busqueda = self._obtener_eventos()

    def restablecer_eventos(self):
        self.eventos_busqueda = self._obtener_eventos()

    def obtener_eventos_busqueda(self):
        return self.eventos_busqueda

    def buscar_eventos(self, criterio, texto_busqueda):
        self.eventos_busqueda = [evento for evento in self._obtener_eventos() if texto_busqueda in getattr(evento, criterio).lower()]
        return self.eventos_busqueda

    # Privados

    def _obtener_eventos(self):
        return Evento.obtener_eventos(self.app.cliente)
