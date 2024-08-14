from model.usuario import Usuario
from model.review import Review


class ControladorReviews():
    def __init__(self, app, evento=None):
        self.app = app
        self.evento = evento

    # Publicos

    def obtener_evento_actual(self):
        return self.evento

    def recuperar_reviews(self, *args):
        reviews = Review.obtener_reviews_id_evento(self.app.cliente, self.evento._id)
        texto = ""
        for review in reviews:
            id_usuario = review.id_usuario
            usuario = Usuario.obtener_usuario_id(self.app.cliente, id_usuario)
            if not usuario:
                # Eliminar review
                break
            calificacion = review.calificacion
            estrellas = ""
            for i in range(calificacion):
                estrellas += "⭐"
            texto += f"{usuario.nombre_usuario} ({estrellas}):\n{review.comentario}\n\n"
        return texto

    def regresar(self):
        self.app.volver_vista_anterior()
