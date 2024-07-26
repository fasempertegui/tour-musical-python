from controller.controlador_principal import ControladorPrincipal
from model.review import Review


class ControladorEscribirReview(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def _generar_id(self, cliente):
        reviews = Review.obtener_reviews(cliente)
        if len(reviews) > 0:
            id_generada = reviews[-1]._id + 1
        else:
            id_generada = 1000
        return id_generada

    def enviar_review(self, calificacion, comentario):
        id_usuario_actual = self.obtener_usuario_actual()._id
        id_evento = self.obtener_evento_actual()._id
        id_review = self._generar_id(self.app.cliente)
        review = Review(id_review, id_evento, id_usuario_actual, calificacion, comentario)
        Review.agregar_review(self.app.cliente, review)
        self.app.event_generate("<<actualizar_botones>>")
