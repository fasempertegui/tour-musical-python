from controller.controlador_principal import ControladorPrincipal


class ControladorMapa(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def regresar(self):
        self.app.volver_frame_anterior()
