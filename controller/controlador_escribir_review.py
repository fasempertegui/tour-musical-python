from utils.decoradores import requiere_sesion_valida
from utils.utils_sesion import SesionUtils

from model.review import Review

import secrets


class ControladorEscribirReview():
    def __init__(self, app, evento=None):
        self.app = app
        self.evento = evento

    # Publicos

    def obtener_evento_actual(self):
        return self.evento

    @requiere_sesion_valida
    def enviar_review(self, calificacion, comentario):
        id_usuario_actual = SesionUtils.obtener_usuario_sesion(self.app.cliente)._id
        id_evento = self.obtener_evento_actual()._id
        id_review = secrets.randbits(60)
        Review.crear_review(self.app.cliente, id_review, id_evento, id_usuario_actual, calificacion, comentario)
        self._generar_evento_actualizar_botones()

    def regresar(self):
        self.app.volver_vista_anterior()

    # Privados

    def _generar_evento_actualizar_botones(self):
        self.app.event_generate("<<actualizar_botones>>")
