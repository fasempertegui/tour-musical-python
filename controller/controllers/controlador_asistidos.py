from controller.controllers.controlador_eventos import ControladorEventos


class ControladorAsistidos(ControladorEventos):
    def __init__(self, app, **datos):
        super().__init__(app, **datos)

    def obtener_eventos_asistidos(self):
        lista = []
        eventos_asistidos = self.obtener_sesion().historial_eventos
        for id_evento in eventos_asistidos:
            e = self.obtener_evento_id(id_evento)
            lista.append(e)
        return lista