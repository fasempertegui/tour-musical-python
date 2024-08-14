import datetime
from controller.controlador_eventos import ControladorEventos


class ControladorExplorar(ControladorEventos):

    def __init__(self, app):
        super().__init__(app)

    def obtener_eventos_futuros(self):
        eventos = super().obtener_eventos()
        return [evento for evento in eventos if evento.hora_inicio > datetime.datetime.utcnow()]

    def obtener_eventos_finalizados(self):
        eventos = super().obtener_eventos()
        return [evento for evento in eventos if evento.hora_inicio < datetime.datetime.utcnow()]
