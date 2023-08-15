class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def ir_a_explorar(self):
        self.app.cambiar_frame(self.app.vista_explorar)

    def ir_a_busqueda(self):
        self.app.cambiar_frame(self.app.vista_busqueda)

    def ir_a_asistidos(self):
        self.app.cambiar_frame(self.app.vista_asistidos)