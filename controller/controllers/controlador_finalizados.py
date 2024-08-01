from controller.controlador_principal import ControladorPrincipal
from model.sesion import Sesion

from view.views.vista_reviews import VistaReviews
from controller.controllers.controlador_reviews import ControladorReviews

from view.views.vista_escribir_review import VistaEscribirReview
from controller.controllers.controlador_escribir_review import ControladorEscribirReview


class ControladorFinalizados(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    # Metodos publicos

    def determinar_usuario_puede_opinar(self):
        id_evento = self.obtener_evento_actual()._id
        reviews = self.obtener_reviews_id_evento(id_evento)
        if not len(reviews) > 0:
            return True
        id_usuario_actual = self.obtener_usuario_actual()._id
        return next((False for review in reviews if review.id_usuario == id_usuario_actual), True)

    def determinar_usuario_asistio(self):
        id_evento = self.obtener_evento_actual()._id
        usuario_actual = self.obtener_usuario_actual()
        return id_evento in usuario_actual.historial_eventos

    def confirmar_asistencia(self):
        id_evento = self.obtener_evento_actual()._id
        cliente = self.app.cliente
        Sesion.actualizar_eventos_asistidos(cliente, id_evento)
        self.app.event_generate("<<actualizar_botones>>")
        self.app.event_generate("<<actualizar_asistidos>>")

    # Navegacion

    def ir_a_reviews(self):
        controlador_reviews = ControladorReviews(self.app)
        vista_reviews = VistaReviews(self.app, controlador_reviews)
        self.app.cambiar_frame(vista_reviews)
        self.app.event_generate("<<ir_reviews>>")

    def ir_a_escribir_review(self):
        controlador_escribir_reviews = ControladorEscribirReview(self.app)
        vista_escribir_review = VistaEscribirReview(self.app, controlador_escribir_reviews)
        self.app.cambiar_frame(vista_escribir_review)
        self.app.event_generate("<<ir_escribir_review>>")

    def regresar(self):
        self.app.volver_frame_anterior()
