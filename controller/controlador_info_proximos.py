from controller.controlador_principal_info import ControladorPrincipalInfo


class ControladorInfoProximos(ControladorPrincipalInfo):

    def __init__(self, app):
        super().__init__(app)

    def ver_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)