import os
from datetime import datetime

class Evento:

    evento_actual = None
    coleccion_actual = os.getenv("COL_EVENTOS")

    def __init__(self, _id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self._id = _id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    @classmethod
    def obtener_eventos(cls, cliente):
        coleccion = cliente[cls.coleccion_actual]
        data = list(coleccion.find())
        return [cls(**evento) for evento in data]

    @classmethod
    def agregar_evento(cls, cliente, evento):
        coleccion = cliente[cls.coleccion_actual]
        coleccion.insert_one(evento.__dict__)

    @classmethod
    def establecer_evento_actual(cls, evento):
        cls.evento_actual = evento

    @classmethod
    def obtener_evento_actual(cls):
        return cls.evento_actual

    @classmethod
    def obtener_eventos_proximos(cls, cliente):
        coleccion = cliente[cls.coleccion_actual]
        fecha_actual = datetime.now().replace(microsecond=0).isoformat()
        data = list(coleccion.find({"hora_inicio": {"$gte": fecha_actual}}))
        return [cls(**evento) for evento in data]

    @classmethod
    def obtener_eventos_finalizados(cls, cliente):
        coleccion = cliente[cls.coleccion_actual]
        fecha_actual = datetime.now().replace(microsecond=0).isoformat()
        data = list(coleccion.find({"hora_inicio": {"$lt": fecha_actual}}))
        return [cls(**evento) for evento in data]

    @classmethod
    def obtener_evento_id(cls, cliente, id):
        coleccion = cliente[cls.coleccion_actual]
        data = coleccion.find_one({"_id": id})
        if data is not None:
            return cls(**data)
        else:
            return None
