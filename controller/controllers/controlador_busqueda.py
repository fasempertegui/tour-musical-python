from controller.controllers.controlador_eventos import ControladorEventos


class ControladorBusqueda(ControladorEventos):
    def __init__(self, app):
        super().__init__(app)
        self.lista_eventos_filtrados = super().obtener_eventos()

    # Implementacion propia
    def obtener_eventos(self):
        return self.lista_eventos_filtrados
    
    def restablecer_eventos(self):
        self.lista_eventos_filtrados = super().obtener_eventos()

    def buscar_eventos(self, criterio, texto_busqueda):
        eventos_filtrados = [evento for evento in self.obtener_eventos() if texto_busqueda in getattr(evento, criterio).lower()]
        self.lista_eventos_filtrados = eventos_filtrados
        return eventos_filtrados