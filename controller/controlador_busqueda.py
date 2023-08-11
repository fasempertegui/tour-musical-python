from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorBusqueda(ControladorPrincipalEventos):
    def __init__(self, app):
        super().__init__(app)
        self.lista_eventos_busqueda = self.app.lista_eventos

    def obtener_eventos(self):
        return self.lista_eventos_busqueda

    def seleccionar_evento(self, indice):
        lista = self.lista_eventos_busqueda
        self._seleccionar_evento(indice, lista)

    def filtrar_eventos(self, criterio, texto_busqueda):
        eventos_filtrados = []
        for evento in self.lista_eventos:
            if texto_busqueda in getattr(evento, criterio).lower():
                eventos_filtrados.append(evento)
        self.lista_eventos_busqueda = eventos_filtrados
