from controller.controlador_principal import ControladorPrincipal
from model.evento import Evento
from model.ubicacion import Ubicacion


class ControladorEventos(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def establecer_evento_actual(self, evento):
        Evento.establecer_evento_actual(evento)

    def establecer_ubicacion_actual(self, ubicacion):
        Ubicacion.establecer_ubicacion_actual(ubicacion)

    def seleccionar_evento(self, evento):
        if evento is not None:
            id_ubicacion = evento.id_ubicacion
            ubicacion = self.obtener_ubicacion_id(id_ubicacion)
            if ubicacion is not None:
                self.establecer_evento_actual(evento)
                self.establecer_ubicacion_actual(ubicacion)
                if evento in self.obtener_eventos_proximos():
                    self.app.event_generate("<<InicializarProximos>>")
                    self.app.cambiar_frame(self.app.vista_proximos)
                else:
                    self.app.event_generate("<<InicializarFinalizados>>")
                    self.app.cambiar_frame(self.app.vista_finalizados)
