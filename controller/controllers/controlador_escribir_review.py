import json

from controller.controlador_principal import ControladorPrincipal
from model.review import Review


class ControladorEscribirReview(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    # Metodos privados

    def _generar_id(self):
        ultima_review = self.obtener_reviews()[-1].id if len(self.obtener_reviews()) > 0 else 999
        return ultima_review + 1

    # Metodos publicos

    def enviar_review(self, calificacion, comentario):
        id_sesion = self.obtener_sesion().id
        id_evento = self.obtener_evento_actual().id
        id_review = self._generar_id()
        review = Review(id_review, id_evento, id_sesion, calificacion, comentario)
        self.agregar_review(review)
        with open("data/reviews.json", "w") as f:
            data = [review.__dict__ for review in self.obtener_reviews()]
            json.dump(data, f, indent=4)
        self.app.event_generate("<<VistaFinalizados>>")
        self.regresar()
