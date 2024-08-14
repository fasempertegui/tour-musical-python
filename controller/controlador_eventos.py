import datetime

from model.evento import Evento
from model.ubicacion import Ubicacion


class ControladorEventos():
    def __init__(self, app):
        self.app = app

    # Metodos comunes de las subclases

    def ir_evento_seleccionado(self, evento):
        if evento is not None:
            id_ubicacion = evento.id_ubicacion
            ubicacion = Ubicacion.obtener_ubicacion_id(self.app.cliente, id_ubicacion)
            if ubicacion is not None:
                if self._es_evento_futuro(evento):
                    self.app.ir_a_futuros(evento, ubicacion)
                else:
                    self.app.ir_a_finalizados(evento)

    def obtener_eventos(self):
        return Evento.obtener_eventos(self.app.cliente)

    # Navegacion

    def regresar(self):
        self.app.volver_vista_anterior()

    # Privados

    def _es_evento_futuro(self, evento):
        return evento.hora_inicio > datetime.datetime.utcnow()
