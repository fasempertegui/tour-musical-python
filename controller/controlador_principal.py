from datetime import datetime


class ControladorPrincipal:
    def __init__(self, app, eventos, ubicaciones, reviews, usuarios, sesion):
        self.app = app
        self.eventos = eventos
        self.ubicaciones = ubicaciones
        self.reviews = reviews
        self.usuarios = usuarios
        self.sesion = sesion

        self.eventos_proximos = []
        self.eventos_finalizados = []

        self._inicializar()

    # Metodos "privados"

    def _inicializar(self):
        hoy = datetime.now().replace(microsecond=0).isoformat()
        for evento in self.obtener_eventos():
            if evento.hora_inicio > hoy:
                self.eventos_proximos.append(evento)
            else:
                self.eventos_finalizados.append(evento)

    # Metodos publicos

    def agregar_review(self, review):
        self.reviews.append(review)

    # Getters
    
    def obtener_evento_actual(self):
        return self.app.evento_actual
    
    def obtener_ubicacion_actual(self):
        return self.app.ubicacion_actual

    def obtener_eventos(self):
        return self.eventos

    def obtener_eventos_proximos(self):
        return self.eventos_proximos

    def obtener_eventos_finalizados(self):
        return self.eventos_finalizados
    
    def obtener_ubicaciones(self):
        return self.ubicaciones
    
    def obtener_reviews(self):
        return self.reviews
    
    def obtener_usuarios(self):
        return self.usuarios
    
    def obtener_sesion(self):
        return self.sesion
    
    def obtener_evento_id(self, id):
        return next((evento for evento in self.obtener_eventos() if evento.id == id), None)
    
    def obtener_eventos_id_ubicacion(self, id_ubicacion):
        return list(evento for evento in self.obtener_eventos() if evento.id_ubicacion == id_ubicacion)

    def obtener_ubicacion_id(self, id):
        return next((ubicacion for ubicacion in self.obtener_ubicaciones() if ubicacion.id == id), None)

    def obtener_review_id(self, id):
        return next((review for review in self.obtener_reviews() if review.id == id), None)
    
    def obtener_reviews_id_usuario(self, id_usuario):
        return list(review for review in self.obtener_reviews() if review.id_usuario == id_usuario)
    
    def obtener_reviews_id_evento(self, id_evento):
        return list(review for review in self.obtener_reviews() if review.id_evento == id_evento)
    
    def obtener_usuario_id(self, id):
        return next((usuario for usuario in self.obtener_usuarios() if usuario.id == id), None)
    
    def obtener_usuarios_evento(self, id_evento):
        return list(usuario for usuario in self.obtener_usuarios() if id_evento in usuario.historial_eventos)
    
    # Setters
    
    def establecer_evento_actual(self, evento):
        self.app.evento_actual = evento

    def establecer_ubicacion_actual(self, ubicacion):
        self.app.ubicacion_actual = ubicacion

    # Navegacion

    def regresar(self):
        self.app.volver_frame_anterior()
