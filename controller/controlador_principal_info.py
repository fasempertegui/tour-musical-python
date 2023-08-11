'''

No me parece necesario utilizar una clase padre ya que la cantidad de metodos compartidos (y no compartidos) es pequeña

'''


class ControladorPrincipalInfo:
    def __init__(self, app, lista_eventos, lista_reviews, usuario_logueado):
        self.app = app
        self.lista_eventos = lista_eventos
        self.lista_reviews = lista_reviews
        self.usuario_logueado = usuario_logueado
        self.lista_reviews_usuario = []
        self._lista_reviews_usuario()

    def _lista_reviews_usuario(self):
        usuario = self.obtener_usuario_logueado()
        id_usuario = usuario.id
        for review in self.obtener_reviews():
            if review.id_usuario == id_usuario:
                self.lista_reviews_usuario.append(review)
                
    def determinar_usuario_puede_opinar(self, asistio, evento):
        if not asistio:
            return False
        reviews = self.obtener_reviews_usuario()
        for review in reviews:
            if review.id_evento == evento.id:
                return True
        return False

    def determinar_usuario_asistio(self, evento):
        usuario = self.obtener_usuario_logueado()
        for id_evento in usuario.historial_eventos:
            if id_evento == evento.id:
                return True
        return False
    
    def obtener_usuario_logueado(self):
        return self.usuario_logueado
    
    def obtener_reviews(self):
        return self.lista_reviews

    def obtener_reviews_usuario(self):
        return self.lista_reviews_usuario

    def ver_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)

    def mostrar_reviews(self):
        self.app.cambiar_frame(self.app.vista_reviews)

    def regresar(self):
        self.app.volver_frame_anterior()
