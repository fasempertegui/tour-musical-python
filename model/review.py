import os


class Review:

    def __init__(self, _id, id_evento, id_usuario, calificacion, comentario):
        self._id = _id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.comentario = comentario
        self.calificacion = calificacion

    @classmethod
    def crear_review(cls, cliente, id_review, id_evento, id_usuario_actual, calificacion, comentario):
        review = cls(id_review, id_evento, id_usuario_actual, calificacion, comentario)
        coleccion = cliente[os.getenv("BD_REVIEWS")]
        coleccion.insert_one(review.__dict__)

    @classmethod
    def obtener_reviews(cls, cliente):
        coleccion = cliente[os.getenv("BD_REVIEWS")]
        data = list(coleccion.find())
        return [cls(**review) for review in data]

    @classmethod
    def obtener_reviews_id_evento(cls, cliente, id_evento):
        coleccion = cliente[os.getenv("BD_REVIEWS")]
        data = list(coleccion.find({"id_evento": id_evento}))
        return [cls(**review) for review in data]
