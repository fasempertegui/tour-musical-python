import os


class Ubicacion:

    def __init__(self, _id, nombre, direccion, coordenadas):
        self._id = _id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    # @classmethod
    # def obtener_ubicaciones(cls, cliente):
    #     coleccion = cliente[os.getenv("BD_UBICACIONES")]
    #     data = list(coleccion.find())
    #     return [cls(**ubicacion) for ubicacion in data]

    @classmethod
    def obtener_ubicacion_id(cls, cliente, id):
        coleccion = cliente[os.getenv("BD_UBICACIONES")]
        data = coleccion.find_one({"_id": id})
        return cls(**data) if data else None

    # @classmethod
    # def insertar_ubicacion(cls, cliente, ubicacion):
    #     coleccion = cliente[os.getenv("BD_UBICACIONES")]
    #     coleccion.insert_one(ubicacion.__dict__)
