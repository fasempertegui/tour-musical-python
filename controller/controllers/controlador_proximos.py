from controller.controlador_principal import ControladorPrincipal


class ControladorProximos(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    # Navegacion

    def ir_a_mapa(self):
        self.app.event_generate("<<Mapa>>")
        self.app.cambiar_frame(self.app.vista_mapa)

    def regresar(self):
        self.app.volver_frame_anterior()
