from controller.controlador_principal import ControladorPrincipal


class ControladorFinalizados(ControladorPrincipal):
    def __init__(self, app, **datos):
        super().__init__(app, **datos)

    # Metodos publicos
                
    def determinar_usuario_puede_opinar(self, asistio):
        id_evento = self.obtener_evento_actual().id
        if not asistio:
            return False
        id_sesion = self.obtener_sesion().id
        reviews = self.obtener_reviews_id_evento(id_evento)
        return next((True for review in reviews if review.id_usuario == id_sesion), False)

    def determinar_usuario_asistio(self):
        id_evento = self.obtener_evento_actual().id
        id_sesion = self.obtener_sesion().id
        usuarios_evento = self.obtener_usuarios_evento(id_evento)
        return next((True for usuario in usuarios_evento if usuario.id == id_sesion), False)
    
    # Navegacion

    def ir_a_reviews(self):
        self.app.event_generate("<<IrReviews>>")
        self.app.cambiar_frame(self.app.vista_reviews)

    def ir_a_escribir_review(self):
        self.app.cambiar_frame(self.app.vista_escribir_review)

    def regresar(self):
        self.app.volver_frame_anterior()
