from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorBusqueda(ControladorPrincipalEventos):
    def __init__(self, app):
        super().__init__(app)
        # Para que la lista de eventos buscados no empiece en blanco se le asigna inicialmente la lista de todos los eventos
        self.lista_eventos_busqueda = self.app.lista_eventos

    def buscar_eventos(self, criterio, texto_busqueda):
        eventos_filtrados = []
        for evento in self.app.lista_eventos:
            if texto_busqueda in getattr(evento, criterio).lower():
                eventos_filtrados.append(evento)
        self.lista_eventos_busqueda = eventos_filtrados
        return eventos_filtrados
    
    def obtener_eventos(self):
        return self.app.lista_eventos

    def obtener_eventos_busqueda(self):
        return self.lista_eventos_busqueda