'''

No me parece necesario utilizar una clase padre ya que la cantidad de metodos compartidos (y no compartidos) es pequeña

'''


class ControladorPrincipalInfo:
    def __init__(self, app):
        self.app = app

    # ver_mapa es utilizado solo por la vista de eventos proximos
    def ver_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)

    # mostrar_reviews, en cambio, solo por la vista de eventos finalizados
    def mostrar_reviews(self):
        self.app.cambiar_frame(self.app.vista_reviews)

    def regresar(self):
        self.app.volver_frame_anterior()
