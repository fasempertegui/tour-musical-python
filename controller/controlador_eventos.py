from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorEventos(ControladorPrincipalEventos):
    def __init__(self, app, lista_eventos, lista_ubicaciones):
        super().__init__(app, lista_eventos, lista_ubicaciones)

    def seleccionar_evento(self, indice, eventos):
        self._seleccionar_evento(indice, eventos)