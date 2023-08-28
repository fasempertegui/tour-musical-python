from controller.controlador_principal import ControladorPrincipal


class ControladorLogin(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def ir_a_inicio(self):
        self.app.event_generate("<<Login>>")