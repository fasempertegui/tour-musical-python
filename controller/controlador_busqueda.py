from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorBusqueda(ControladorPrincipalEventos):
    def __init__(self, app, lista_eventos, lista_ubicaciones):
        super().__init__(app, lista_eventos, lista_ubicaciones)
        # Lista de eventos propia de la subclase
        self.lista_eventos_busqueda = lista_eventos

    def seleccionar_evento(self, indice):
        lista = self.lista_eventos_busqueda
        self._seleccionar_evento(indice, lista)

    def buscar_eventos(self, criterio, texto_busqueda):
        eventos_filtrados = []
        for evento in self.lista_eventos:
            if texto_busqueda in getattr(evento, criterio).lower():
                eventos_filtrados.append(evento)
        self.lista_eventos_busqueda = eventos_filtrados
        return eventos_filtrados