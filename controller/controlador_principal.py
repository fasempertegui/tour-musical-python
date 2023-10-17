from model.evento import Evento
from model.ubicacion import Ubicacion
from model.review import Review
from model.usuario import Usuario, Sesion


class ControladorPrincipal:
    def __init__(self, app):
        self.app = app

    # Getters

    def obtener_eventos(self):
        return Evento.obtener_eventos()

    def obtener_eventos_proximos(self):
        return Evento.obtener_eventos_proximos()

    def obtener_eventos_finalizados(self):
        return Evento.obtener_eventos_finalizados()

    def obtener_evento_actual(self):
        return Evento.obtener_evento_actual()

    def obtener_evento_id(self, id):
        return Evento.obtener_evento_id(id)

    # def obtener_eventos_id_ubicacion(self, id_ubicacion):
    #     return Evento.obtener_eventos_id_ubicacion(id_ubicacion)

    def obtener_ubicaciones(self):
        return Ubicacion.obtener_ubicaciones()

    def obtener_ubicacion_id(self, id):
        return Ubicacion.obtener_ubicacion_id(id)

    def obtener_ubicacion_actual(self):
        return Ubicacion.obtener_ubicacion_actual()

    def obtener_reviews(self):
        return Review.obtener_reviews()

    # def obtener_review_id(self, id):
    #     return Review.obtener_review_id(id)

    # def obtener_reviews_id_usuario(self, id_usuario):
    #     return Review.obtener_reviews_id_usuario(id_usuario)

    def obtener_reviews_id_evento(self, id_evento):
        return Review.obtener_reviews_id_evento(id_evento)

    def obtener_usuarios(self):
        return Usuario.obtener_usuarios()

    def obtener_usuario_id(self, id):
        return Usuario.obtener_usuario_id(id)

    # def obtener_usuarios_evento(self, id_evento):
    #     return Usuario.obtener_usuarios_evento(id_evento)

    def obtener_usuario_actual(self):
        return Sesion.obtener_usuario_actual()

    # Navegacion

    def regresar(self):
        self.app.volver_frame_anterior()
