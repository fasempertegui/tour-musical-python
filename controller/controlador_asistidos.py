from controller.controlador_eventos import ControladorEventos

from model.evento import Evento

from utils.utils_sesion import SesionUtils


class ControladorAsistidos(ControladorEventos):

    def __init__(self, app):
        super().__init__(app)

    def obtener_eventos_asistidos(self):
        usuario_actual = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        if usuario_actual:
            eventos_asistidos = usuario_actual.historial_eventos
            return [self._obtener_evento_id(id_evento) for id_evento in eventos_asistidos]
        else:
            print("El usuario no existe o la sesion es invalida")
            return None

    # Privados

    def _obtener_evento_id(self, id):
        return Evento.obtener_evento_id(self.app.cliente, id)
