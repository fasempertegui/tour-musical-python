class ControladorReviews:
    def __init__(self, app, lista_usuarios, lista_reviews):
        self.app = app
        self.lista_usuarios = lista_usuarios
        self.lista_reviews = lista_reviews

    # Metodo privado
    def _obtener_reviews_evento(self, evento):
        lista = []
        for review in self.obtener_reviews():
            if review.id_evento == evento.id:
                lista.append(review)
        return lista
    
    def _obtener_usuario_id(self, id_usuario):
        for usuario in self.obtener_usuarios():
            if usuario.id == id_usuario:
                return usuario

    def recuperar_reviews(self, evento):
        reviews = self._obtener_reviews_evento(evento)
        texto = ""
        for review in reviews:
            id_usuario = review.id_usuario
            usuario = self._obtener_usuario_id(id_usuario)
            calificacion = review.calificacion
            estrellas = ""
            for i in range(calificacion):
                estrellas += "⭐"
            texto += f"{usuario.nombre_usuario} ({estrellas}):\n{review.comentario}\n\n"
        return texto

    def obtener_usuarios(self):
        return self.lista_usuarios
    
    def obtener_reviews(self):
        return self.lista_reviews

    def regresar(self):
        self.app.volver_frame_anterior()
