import os
from datetime import datetime


class Evento:

    def __init__(self, _id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self._id = _id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = datetime.strptime(hora_inicio, "%Y-%m-%dT%H:%M:%S")
        self.hora_fin = datetime.strptime(hora_fin, "%Y-%m-%dT%H:%M:%S")
        self.descripcion = descripcion
        self.imagen = imagen

    @classmethod
    def obtener_eventos(cls, cliente):
        coleccion = cliente[os.getenv("BD_EVENTOS")]
        data = list(coleccion.find())
        return [cls(**evento) for evento in data]

    @classmethod
    def obtener_evento_id(cls, cliente, id):
        coleccion = cliente[os.getenv("BD_EVENTOS")]
        data = coleccion.find_one({"_id": id})
        return cls(**data) if data else None

    # @classmethod
    # def insertar_evento(cls, cliente, evento):
    #     coleccion = cliente[os.getenv("BD_EVENTOS")]
    #     coleccion.insert_one(evento.__dict__)
