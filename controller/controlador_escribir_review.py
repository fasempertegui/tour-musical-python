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
        usuario_actual = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        if usuario_actual:
            id_evento = self.obtener_evento_actual()._id
            Review.crear_review(self.app.cliente, id_evento, usuario_actual._id, calificacion, comentario)
            self._generar_evento_actualizar_botones()
        else:
            print("El usuario no existe o la sesion es invalida")

    def regresar(self):
        self.app.volver_vista_anterior()

    # Privados

    def _generar_evento_actualizar_botones(self):
        self.app.event_generate("<<actualizar_botones>>")
