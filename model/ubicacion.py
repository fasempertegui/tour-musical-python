import json


class Ubicacion:

    ubicaciones = []
    ubicacion_actual = None

    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    @classmethod
    def cargar_ubicaciones(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        cls.ubicaciones = [cls(**ubicacion) for ubicacion in data]

    @classmethod
    def establecer_ubicacion_actual(cls, ubicacion):
        cls.ubicacion_actual = ubicacion

    # Getters

    @classmethod
    def obtener_ubicaciones(cls):
        return cls.ubicaciones

    @classmethod
    def obtener_ubicacion_actual(cls):
        return cls.ubicacion_actual

    @classmethod
    def obtener_ubicacion_id(cls, id):
        return next((ubicacion for ubicacion in cls.ubicaciones if ubicacion.id == id), None)
