from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorEventos(ControladorPrincipalEventos):
    def __init__(self, app):
        super().__init__(app)

    def seleccionar_evento(self, indice, eventos):
        self._seleccionar_evento(indice, eventos)