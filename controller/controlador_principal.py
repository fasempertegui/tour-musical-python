from model.evento import Evento
from model.ubicacion import Ubicacion
from model.review import Review
from model.usuario import Usuario
from model.sesion import Sesion


class ControladorPrincipal:
    def __init__(self, app):
        self.app = app

    # Getters

    def obtener_eventos(self):
        return Evento.obtener_eventos(self.app.cliente)

    def obtener_eventos_proximos(self):
        return Evento.obtener_eventos_proximos(self.app.cliente)

    def obtener_eventos_finalizados(self):
        return Evento.obtener_eventos_finalizados(self.app.cliente)

    def obtener_evento_actual(self):
        return Evento.obtener_evento_actual()

    def obtener_evento_id(self, id):
        return Evento.obtener_evento_id(self.app.cliente, id)

    def obtener_ubicaciones(self):
        return Ubicacion.obtener_ubicaciones(self.app.cliente)

    def obtener_ubicacion_id(self, id):
        return Ubicacion.obtener_ubicacion_id(self.app.cliente, id)

    def obtener_ubicacion_actual(self):
        return Ubicacion.obtener_ubicacion_actual()

    def obtener_reviews_id_evento(self, id_evento):
        return Review.obtener_reviews_id_evento(self.app.cliente, id_evento)

    def obtener_usuario_id(self, id):
        return Usuario.obtener_usuario_id(self.app.cliente, id)

    def obtener_usuario_nombre_usuario(self, nombre_usuario):
        return Usuario.obtener_usuario_nombre_usuario(self.app.cliente, nombre_usuario)

    def obtener_usuario_actual(self):
        return Sesion.obtener_usuario_actual()
    
    def obtener_configuracion_usuario(self):
        return Sesion.obtener_usuario_actual().obtener_configuracion_usuario()

    # Navegacion

    def regresar(self):
        self.app.volver_frame_anterior()
