import json


class Usuario:

    usuarios = []
    sesion = None

    def __init__(self, id, nombre_usuario, historial_eventos):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.historial_eventos = historial_eventos

    @classmethod
    def cargar_usuarios(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        cls.usuarios = [cls(**usuario) for usuario in data]
        cls.sesion = cls.usuarios[0]

    @classmethod
    def agregar_usuario(cls, usuario):
        cls.usuarios.append(usuario)

    # Getters

    @classmethod
    def obtener_usuarios(cls):
        return cls.usuarios

    @classmethod
    def obtener_usuario_id(cls, id):
        return next((usuario for usuario in cls.usuarios if usuario.id == id), None)

    @classmethod
    def obtener_usuarios_evento(cls, id_evento):
        return list(usuario for usuario in cls.usuarios if id_evento in usuario.historial_eventos)
    
    @classmethod
    def obtener_sesion(cls):
        return cls.sesion
