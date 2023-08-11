from controller.controlador_eventos import ControladorEventos


class ControladorBusqueda(ControladorEventos):
    def __init__(self, app, lista_eventos, lista_ubicaciones):
        super().__init__(app, lista_eventos, lista_ubicaciones)
        # Para que la lista de eventos buscados no empiece en blanco se le asigna inicialmente la lista de todos los eventos
        self.lista_eventos_busqueda = self.lista_eventos

    def buscar_eventos(self, criterio, texto_busqueda):
        eventos_filtrados = []
        for evento in self.obtener_eventos():
            if texto_busqueda in getattr(evento, criterio).lower():
                eventos_filtrados.append(evento)
        self.lista_eventos_busqueda = eventos_filtrados
        return eventos_filtrados

    def obtener_eventos_buscados(self):
        return self.lista_eventos_busqueda