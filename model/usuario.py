import os
import bcrypt
import secrets


class Usuario:

    def __init__(self, _id, nombre_usuario, contrasena, historial_eventos, configuracion_usuario):
        self._id = _id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.historial_eventos = historial_eventos
        self.configuracion_usuario = configuracion_usuario

    @classmethod
    def obtener_usuarios(cls, cliente):
        bd_usuarios = os.getenv("BD_USUARIOS")
        data = list(cliente[bd_usuarios].find())
        return [cls(**usuario) for usuario in data]

    @classmethod
    def obtener_usuario_id(cls, cliente, id):
        bd_usuarios = os.getenv("BD_USUARIOS")
        usuario = cliente[bd_usuarios].find_one({"_id": id})
        return cls(**usuario)

    @classmethod
    def obtener_usuario_nombre_usuario(cls, cliente, nombre_usuario):
        bd_usuarios = os.getenv("BD_USUARIOS")
        usuario = cliente[bd_usuarios].find_one({"nombre_usuario": nombre_usuario})
        return cls(**usuario) if usuario else None

    @classmethod
    def crear_usuario(cls, cliente, nombre_usuario, contrasena):
        hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
        id_generada = secrets.randbits(56)
        nuevo_usuario = Usuario(id_generada, nombre_usuario, hashed_password, [], {"ubicacion": None})
        bd_usuarios = os.getenv("BD_USUARIOS")
        cliente[bd_usuarios].insert_one(nuevo_usuario.__dict__)
        return nuevo_usuario

    @classmethod
    def actualizar_eventos(cls, cliente, id_usuario, id_evento):
        filtro = {"_id": id_usuario}
        usuario = cls.obtener_usuario_id(cliente, id_usuario)
        if usuario:
            usuario.historial_eventos.append(id_evento)
            actualizacion = {"$set": {"historial_eventos": usuario.historial_eventos}}
            bd_usuarios = os.getenv("BD_USUARIOS")
            cliente[bd_usuarios].update_one(filtro, actualizacion)

    @classmethod
    def actualizar_configuracion(cls, cliente, id_usuario, coordenadas):
        filtro = {"_id": id_usuario}
        actualizacion = {"$set": {"configuracion_usuario": {"ubicacion": coordenadas}}}
        bd_usuarios = os.getenv("BD_USUARIOS")
        cliente[bd_usuarios].update_one(filtro, actualizacion)

    def validar_credenciales(self, contrasena):
        return bcrypt.checkpw(contrasena.encode('utf-8'), self.contrasena)

    def obtener_configuracion_usuario(self):
        return self.configuracion_usuario
