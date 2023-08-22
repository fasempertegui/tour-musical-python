from model.evento import Evento
from model.ubicacion import Ubicacion
from model.review import Review
from model.usuario import Usuario, Sesion


class ControladorPrincipal:
    def __init__(self, app):
        self.app = app
        Evento.cargar_eventos(self.app.cliente)
        Ubicacion.cargar_ubicaciones(self.app.cliente)
        Review.cargar_reviews(self.app.cliente)
        Usuario.cargar_usuarios(self.app.cliente)

    def autenticar(self, nombre_usuario, contrasena):
        return Sesion.autenticar(nombre_usuario, contrasena)
    
    def registrar(self, nombre_usuario, contrasena):
        return Sesion.registrar(self.app.cliente, nombre_usuario, contrasena)
    
    def cerrar_sesion(self):
        Sesion.cerrar_sesion()

    def agregar_review(self, review):
        Review.agregar_review(self.app.cliente, review)

    def actualizar_eventos_asistidos(self, id_evento):
        Sesion.actualizar_eventos_asistidos(self.app.cliente, id_evento)

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
    
    def obtener_eventos_id_ubicacion(self, id_ubicacion):
        return Evento.obtener_eventos_id_ubicacion(id_ubicacion)
    
    def obtener_ubicaciones(self):
        return Ubicacion.obtener_ubicaciones()
    
    def obtener_ubicacion_id(self, id):
        return Ubicacion.obtener_ubicacion_id(id)
    
    def obtener_ubicacion_actual(self):
        return Ubicacion.obtener_ubicacion_actual()

    def obtener_reviews(self):
        return Review.obtener_reviews()
    
    def obtener_review_id(self, id):
        return Review.obtener_review_id(id)
    
    def obtener_reviews_id_usuario(self, id_usuario):
        return Review.obtener_reviews_id_usuario(id_usuario)
    
    def obtener_reviews_id_evento(self, id_evento):
        return Review.obtener_reviews_id_evento(id_evento)
    
    def obtener_usuarios(self):
        return Usuario.obtener_usuarios()
    
    def obtener_usuario_id(self, id):
        return Usuario.obtener_usuario_id(id)
    
    def obtener_usuarios_evento(self, id_evento):
        return Usuario.obtener_usuarios_evento(id_evento)
    
    def obtener_usuario_actual(self):
        return Sesion.obtener_usuario_actual()

    # Setters
    
    def establecer_evento_actual(self, evento):
        Evento.establecer_evento_actual(evento)

    def establecer_ubicacion_actual(self, ubicacion):
        Ubicacion.establecer_ubicacion_actual(ubicacion)

    # Navegacion

    def regresar(self):
        self.app.volver_frame_anterior()
