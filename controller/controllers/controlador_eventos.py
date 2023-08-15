from controller.controlador_principal import ControladorPrincipal

class ControladorEventos(ControladorPrincipal):
    def __init__(self, app, **datos):
        super().__init__(app, **datos)

    def seleccionar_evento(self, evento):
        if evento is not None:
            id_ubicacion = evento.id_ubicacion
            ubicacion = self.obtener_ubicacion_id(id_ubicacion)
            if ubicacion is not None:
                self.establecer_evento_actual(evento)
                self.establecer_ubicacion_actual(ubicacion)
                #
                if evento in self.obtener_eventos_proximos():
                    self.app.event_generate("<<VistaProximos>>")
                    self.app.cambiar_frame(self.app.vista_proximos)
                else:
                    self.app.event_generate("<<VistaFinalizados>>")
                    self.app.cambiar_frame(self.app.vista_finalizados)