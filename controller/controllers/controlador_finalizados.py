import json

from controller.controlador_principal import ControladorPrincipal


class ControladorFinalizados(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    # Metodos publicos

    def determinar_usuario_puede_opinar(self):
        id_evento = self.obtener_evento_actual().id
        reviews = self.obtener_reviews_id_evento(id_evento)
        if not len(reviews) > 0:
            # Nadie opino
            return True
        id_sesion = self.obtener_sesion().id
        return next((False for review in reviews if review.id_usuario == id_sesion), True)

    def determinar_usuario_asistio(self):
        id_evento = self.obtener_evento_actual().id
        sesion = self.obtener_sesion()
        return id_evento in sesion.historial_eventos

    def confirmar_asistencia(self):
        id_evento = self.obtener_evento_actual().id
        self.obtener_sesion().historial_eventos.append(id_evento)
        with open("data/usuarios.json", "w") as f:
            data = [usuario.__dict__ for usuario in self.obtener_usuarios()]
            json.dump(data, f, indent=8)
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
