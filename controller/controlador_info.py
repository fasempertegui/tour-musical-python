
class ControladorInfo:
    def __init__(self, app):
        self.app = app

    def ver_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)

    def regresar(self):
        self.app.volver_frame_anterior()