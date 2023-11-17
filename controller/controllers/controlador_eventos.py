from controller.controlador_principal import ControladorPrincipal
from model.evento import Evento
from model.ubicacion import Ubicacion

from view.views.vista_proximos import VistaProximos
from controller.controllers.controlador_proximos import ControladorProximos

from view.views.vista_finalizados import VistaFinalizados
from controller.controllers.controlador_finalizados import ControladorFinalizados


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
                proximos = self.obtener_eventos_proximos()
                encontrado = next((True for e in proximos if e._id == evento._id), False)
                if encontrado:
                    controlador_proximos = ControladorProximos(self.app)
                    vista_proximos = VistaProximos(self.app, controlador_proximos)
                    self.app.cambiar_frame(vista_proximos)
                    self.app.event_generate("<<InicializarProximos>>")
                else:
                    controlador_finalizados = ControladorFinalizados(self.app)
                    vista_finalizados = VistaFinalizados(self.app, controlador_finalizados)
                    self.app.cambiar_frame(vista_finalizados)
                    self.app.event_generate("<<InicializarFinalizados>>")