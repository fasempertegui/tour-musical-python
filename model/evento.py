import json
from datetime import datetime


class Evento:

    eventos = []
    evento_actual = None

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
    def cargar_eventos(cls, cliente):
        coleccion = cliente["eventos"]
        data = list(coleccion.find())
        cls.eventos = [cls(**evento) for evento in data]

    @classmethod
    def agregar_evento(cls, evento):
        cls.eventos.append(evento)

    @classmethod
    def establecer_evento_actual(cls, evento):
        cls.evento_actual = evento

    # Getters

    @classmethod
    def obtener_eventos(cls):
        return cls.eventos

    @classmethod
    def obtener_evento_actual(cls):
        return cls.evento_actual

    @classmethod
    def obtener_eventos_proximos(cls):
        fecha_actual = datetime.now().replace(microsecond=0).isoformat()
        return [evento for evento in cls.eventos if evento.hora_inicio >= fecha_actual]

    @classmethod
    def obtener_eventos_finalizados(cls):
        fecha_actual = datetime.now().replace(microsecond=0).isoformat()
        return [evento for evento in cls.eventos if evento.hora_inicio < fecha_actual]

    @classmethod
    def obtener_evento_actual(cls):
        return cls.evento_actual

    @classmethod
    def obtener_evento_id(cls, id):
        return next((evento for evento in cls.eventos if evento._id == id), None)

    @classmethod
    def obtener_eventos_id_ubicacion(cls, id_ubicacion):
        return list(evento for evento in cls.eventos if evento.id_ubicacion == id_ubicacion)
