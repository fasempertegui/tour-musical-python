import json


class Review:
    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.comentario = comentario
        self.calificacion = calificacion
        self.animo = animo

    @classmethod
    def cargar_reviews(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**review) for review in data]
