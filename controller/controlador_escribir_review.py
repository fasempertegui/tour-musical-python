from model.review import Review

class ControladorEscribirReview:
    def __init__(self, app):
        self.app = app
        
    # Referencia al evento??????
    def enviar_review(self, calificacion, comentario):
        review = Review(1003, 1003, 1000, calificacion, comentario)
        print(review.__dict__)
        self.regresar()

    def regresar(self):
        self.app.volver_frame_anterior()
