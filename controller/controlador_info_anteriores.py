from controller.controlador_principal_info import ControladorPrincipalInfo


class ControladorInfoAnteriores(ControladorPrincipalInfo):

    def __init__(self, app):
        super().__init__(app)

    def mostrar_reviews(self):
        self.app.cambiar_frame(self.app.vista_reviews)