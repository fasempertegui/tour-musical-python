import os
import bcrypt


class Usuario:

    def __init__(self, _id, nombre_usuario, contrasena, historial_eventos, configuracion_usuario):
        self._id = _id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.historial_eventos = historial_eventos
        self.configuracion_usuario = configuracion_usuario

    @classmethod
    def obtener_usuarios(cls, cliente):
        coleccion = cliente[os.getenv("BD_USUARIOS")]
        data = list(coleccion.find())
        return [cls(**usuario) for usuario in data]

    @classmethod
    def obtener_usuario_id(cls, cliente, id):
        coleccion = cliente[os.getenv("BD_USUARIOS")]
        usuario = coleccion.find_one({"_id": id})
        return cls(**usuario)

    @classmethod
    def obtener_usuario_nombre_usuario(cls, cliente, nombre_usuario):
        coleccion = cliente[os.getenv("BD_USUARIOS")]
        usuario = coleccion.find_one({"nombre_usuario": nombre_usuario})
        return cls(**usuario) if usuario else None

    @classmethod
    def _generar_id(cls, cliente):
        usuarios = cls.obtener_usuarios(cliente)
        return usuarios[-1]._id + 1 if usuarios else 1000

    @classmethod
    def crear_usuario(cls, cliente, nombre_usuario, contrasena):
        hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
        id_generada = cls._generar_id(cliente)
        nuevo_usuario = Usuario(id_generada, nombre_usuario, hashed_password, [], {"ubicacion": None})
        coleccion = cliente[os.getenv("BD_USUARIOS")]
        coleccion.insert_one(nuevo_usuario.__dict__)
        return nuevo_usuario

    def validar_credenciales(self, contrasena):
        return bcrypt.checkpw(contrasena.encode('utf-8'), self.contrasena)

    def obtener_configuracion_usuario(self):
        return self.configuracion_usuario
