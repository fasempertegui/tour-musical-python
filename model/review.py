import json


class Review:

    reviews = []

    def __init__(self, _id, id_evento, id_usuario, calificacion, comentario):
        self._id = _id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.comentario = comentario
        self.calificacion = calificacion

    @classmethod
    def cargar_reviews(cls, cliente):
        coleccion = cliente["reviews"]
        data = list(coleccion.find())
        cls.reviews = [cls(**review) for review in data]
    
    @classmethod
    def agregar_review(cls, cliente, review):
        coleccion = cliente["reviews"]
        coleccion.insert_one(review.__dict__)
        cls.reviews.append(review)

    # Getters

    @classmethod
    def obtener_reviews(cls):
        return cls.reviews

    # @classmethod
    # def obtener_review_id(cls, id):
    #     return next((review for review in cls.reviews if review._id == id), None)
    
    # @classmethod
    # def obtener_reviews_id_usuario(cls, id_usuario):
    #     return list(review for review in cls.reviews if review.id_usuario == id_usuario)
    
    @classmethod
    def obtener_reviews_id_evento(cls, id_evento):
        return list(review for review in cls.reviews if review.id_evento == id_evento)