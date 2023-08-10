import json


class Usuario:
    def __init__(self, id, nombre_usuario, historial_eventos):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.historial_eventos = historial_eventos

    @classmethod
    def cargar_usuario(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**usuario) for usuario in data]