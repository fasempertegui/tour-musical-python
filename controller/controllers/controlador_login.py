from controller.controlador_principal import ControladorPrincipal


class ControladorLogin(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def renderizar(self):
        self.app.event_generate("<<Login>>")