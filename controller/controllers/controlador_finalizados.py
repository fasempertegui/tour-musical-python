import json

from controller.controlador_principal import ControladorPrincipal


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
        self.actualizar_eventos_asistidos(id_evento)
        self.app.event_generate("<<Asistencia>>")

    # Navegacion

    def ir_a_reviews(self):
        self.app.event_generate("<<IrReviews>>")
        self.app.cambiar_frame(self.app.vista_reviews)

    def ir_a_escribir_review(self):
        self.app.event_generate("<<IrEscribirReviews>>")
        self.app.cambiar_frame(self.app.vista_escribir_review)

    def regresar(self):
        self.app.volver_frame_anterior()
