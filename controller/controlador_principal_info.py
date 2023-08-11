'''

No me parece necesario utilizar una clase padre ya que la cantidad de metodos compartidos (y no compartidos) es pequeña

'''


class ControladorPrincipalInfo:
    def __init__(self, app):
        self.app = app
        self.lista_reviews_usuario = []
        self._lista_reviews_usuario()

    def _lista_reviews_usuario(self):
        id_usuario_logueado = self.app.usuario_logueado.id
        for review in self.app.lista_reviews:
            if review.id_usuario == id_usuario_logueado:
                self.lista_reviews_usuario.append(review)

    def obtener_reviews_usuario(self):
        return self.lista_reviews_usuario

    def obtener_usuario_logueado(self):
        return self.app.usuario_logueado

    # ver_mapa es utilizado solo por la vista de eventos proximos
    def ver_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)

    # mostrar_reviews, en cambio, solo por la vista de eventos finalizados
    def mostrar_reviews(self):
        self.app.cambiar_frame(self.app.vista_reviews)

    def regresar(self):
        self.app.volver_frame_anterior()
