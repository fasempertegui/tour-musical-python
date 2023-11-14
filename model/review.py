import os

class Review:

    coleccion_actual = os.getenv("COL_REVIEWS")

    def __init__(self, _id, id_evento, id_usuario, calificacion, comentario):
        self._id = _id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.comentario = comentario
        self.calificacion = calificacion

    @classmethod
    def obtener_reviews(cls, cliente):
        coleccion = cliente[cls.coleccion_actual]
        data = list(coleccion.find())
        return [cls(**review) for review in data]
    
    @classmethod
    def obtener_reviews_id_evento(cls, cliente, id_evento):
        coleccion = cliente[cls.coleccion_actual]
        data = list(coleccion.find({"id_evento": id_evento}))
        return [cls(**review) for review in data]
    
    @classmethod
    def agregar_review(cls, cliente, review):
        coleccion = cliente[cls.coleccion_actual]
        coleccion.insert_one(review.__dict__)