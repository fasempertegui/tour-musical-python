from datetime import datetime


class ControladorReviews:
    def __init__(self, app, lista_reviews, lista_usuarios):
        self.app = app
        self.lista_usuarios = lista_usuarios
        self.lista_reviews = lista_reviews

    def obtener_nombre_usuario(self, id_usuario):
        for usuario in self.lista_usuarios:
            if usuario.id == id_usuario:
                return usuario.nombre_usuario
        # return None
    
    def obtener_reviews_evento(self, evento):
        lista = []
        for review in self.lista_reviews:
            if review.id_evento == evento.id:
                lista.append(review)
        return lista

    def regresar(self):
        self.app.volver_frame_anterior()
