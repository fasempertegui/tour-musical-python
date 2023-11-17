from controller.controlador_principal import ControladorPrincipal


class ControladorMapa(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def obtener_configuracion_usuario(self):
        return self.obtener_usuario_actual().obtener_configuracion_usuario()

    def regresar(self):
        self.app.volver_frame_anterior()
