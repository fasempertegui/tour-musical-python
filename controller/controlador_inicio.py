class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_eventos(self):
        self.app.cambiar_frame(self.app.vista_eventos)

    def busqueda(self):
        self.app.cambiar_frame(self.app.vista_busqueda)

    def eventos_asistidos(self):
        self.app.cambiar_frame(self.app.vista_asistidos)