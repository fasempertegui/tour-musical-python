class ControladorReviews:
    def __init__(self, app):
        self.app = app

    def obtener_nombre_usuario(self, id_usuario):
        for usuario in self.app.lista_usuarios:
            if usuario.id == id_usuario:
                return usuario.nombre_usuario
        # return None
    
    def obtener_reviews_evento(self, evento):
        lista = []
        for review in self.app.lista_reviews:
            if review.id_evento == evento.id:
                lista.append(review)
        return lista

    def regresar(self):
        self.app.volver_frame_anterior()
