from controller.controlador_principal import ControladorPrincipal


class ControladorReviews(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)
        
    # Metodos publicos

    def recuperar_reviews(self, *args):
        id_evento_actual = self.obtener_evento_actual()._id
        reviews = self.obtener_reviews_id_evento(id_evento_actual)
        texto = ""
        for review in reviews:
            id_usuario = review.id_usuario
            usuario = self.obtener_usuario_id(id_usuario)
            calificacion = review.calificacion
            estrellas = ""
            for i in range(calificacion):
                estrellas += "⭐"
            texto += f"{usuario.nombre_usuario} ({estrellas}):\n{review.comentario}\n\n"
        return texto
