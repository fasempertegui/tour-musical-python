from controller.controlador_eventos import ControladorEventos

from model.evento import Evento

from utils.utils_sesion import SesionUtils


class ControladorAsistidos(ControladorEventos):

    def __init__(self, app):
        super().__init__(app)

    def obtener_eventos_asistidos(self):
        eventos_asistidos = SesionUtils.obtener_usuario_sesion(self.app.cliente).historial_eventos
        return [self._obtener_evento_id(id_evento) for id_evento in eventos_asistidos]

    # Privados

    def _obtener_evento_id(self, id):
        return Evento.obtener_evento_id(self.app.cliente, id)
