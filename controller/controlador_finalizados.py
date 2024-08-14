from controller.controlador_escribir_review import ControladorEscribirReview
from controller.controlador_eventos import ControladorEventos
from controller.controlador_reviews import ControladorReviews

from model.review import Review

from utils.decoradores import requiere_sesion_valida
from utils.utils_sesion import SesionUtils

from view.vista_escribir_review import VistaEscribirReview
from view.vista_reviews import VistaReviews


class ControladorFinalizados(ControladorEventos):

    def __init__(self, app, evento=None):
        super().__init__(app)
        self.evento = evento

    def obtener_evento_actual(self):
        return self.evento

    def determinar_usuario_asistio(self):
        id_evento = self.evento._id
        usuario_actual = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        if usuario_actual:
            return id_evento in usuario_actual.historial_eventos
        else:
            return None

    def determinar_usuario_puede_opinar(self):
        id_evento = self.evento._id
        reviews = self._obtener_reviews_id_evento(id_evento)
        if not len(reviews) > 0:
            return True
        usuario_actual = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        if usuario_actual:
            return next((False for review in reviews if review.id_usuario == usuario_actual._id), True)
        else:
            print("El usuario no existe o la sesion es invalida")
            return None

    @requiere_sesion_valida
    def confirmar_asistencia(self):
        id_evento = self.evento._id
        usuario_actual = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        if usuario_actual:
            usuario_actual.historial_eventos.append(id_evento)
            actualizacion = {"$set": {"historial_eventos": usuario_actual.historial_eventos}}
            usuario_actual.actualizar_usuario(self.app.cliente, actualizacion)
            self.app.event_generate("<<actualizar_botones>>")
            self.app.event_generate("<<actualizar_asistidos>>")
        else:
            print("El usuario no existe o la sesion es invalida")

    # Navegacion

    def ir_a_reviews(self):
        self.app.cambiar_vista(ControladorReviews, VistaReviews, self.evento)

    @requiere_sesion_valida
    def ir_a_escribir_review(self):
        self.app.cambiar_vista(ControladorEscribirReview, VistaEscribirReview, self.evento)

    # Privados

    def _obtener_reviews_id_evento(self, id_evento):
        return Review.obtener_reviews_id_evento(self.app.cliente, id_evento)
