from controller.controllers.controlador_eventos import ControladorEventos


class ControladorBusqueda(ControladorEventos):
    def __init__(self, app, **datos):
        super().__init__(app, **datos)
        # Para que la lista de eventos buscados no empiece en blanco se le asigna inicialmente la lista de todos los eventos
        self.lista_eventos_busqueda = self.obtener_eventos()

    def buscar_eventos(self, criterio, texto_busqueda):
        eventos_filtrados = []
        for evento in self.obtener_eventos():
            if texto_busqueda in getattr(evento, criterio).lower():
                eventos_filtrados.append(evento)
        self.lista_eventos_busqueda = eventos_filtrados
        return eventos_filtrados

    def obtener_eventos_buscados(self):
        return self.lista_eventos_busqueda