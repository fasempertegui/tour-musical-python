from controller.controlador_principal import ControladorPrincipal


class ControladorProximos(ControladorPrincipal):
    def __init__(self, app, **datos):
        super().__init__(app, **datos)

    # Navegacion

    def ir_a_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)

    def regresar(self):
        self.app.volver_frame_anterior()
