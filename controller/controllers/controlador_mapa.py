class ControladorMapa:
    def __init__(self, app):
        self.app = app

    def regresar(self):
        self.app.volver_frame_anterior()