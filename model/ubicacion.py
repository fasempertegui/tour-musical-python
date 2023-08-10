import json


class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def cargar_ubicaciones(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**ubicacion) for ubicacion in data]