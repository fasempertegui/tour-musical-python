import os

class Ubicacion:

    ubicacion_actual = None

    def __init__(self, _id, nombre, direccion, coordenadas):
        self._id = _id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    @classmethod
    def establecer_ubicacion_actual(cls, ubicacion):
        cls.ubicacion_actual = ubicacion

    @classmethod
    def obtener_ubicacion_actual(cls):
        return cls.ubicacion_actual

    @classmethod
    def obtener_ubicaciones(cls, cliente):
        coleccion = cliente[os.getenv("BD_UBICACIONES")]
        data = list(coleccion.find())
        return [cls(**ubicacion) for ubicacion in data]

    @classmethod
    def obtener_ubicacion_id(cls, cliente, id):
        coleccion = cliente[os.getenv("BD_UBICACIONES")]
        data = coleccion.find_one({"_id": id})
        if data is not None:
            return cls(**data)
        else:
            return None

    @classmethod
    def agregar_ubicacion(cls, cliente, ubicacion):
        coleccion = cliente[os.getenv("BD_UBICACIONES")]
        coleccion.insert_one(ubicacion.__dict__)
