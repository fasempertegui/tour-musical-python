import os
import bcrypt
import secrets


class Usuario:

    def __init__(self, nombre_usuario, contrasena, _id=None, historial_eventos=None, configuracion_usuario=None):
        self._id = _id if _id is not None else secrets.randbits(60)
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.historial_eventos = historial_eventos if historial_eventos is not None else []
        self.configuracion_usuario = configuracion_usuario if configuracion_usuario is not None else {"ubicacion": None}

    # Metodos de clase

    @classmethod
    def crear_usuario(cls, cliente, nombre_usuario, contrasena):
        hash = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
        usuario = cls(nombre_usuario, hash)
        cliente[os.getenv("BD_USUARIOS")].insert_one(usuario.__dict__)

    @classmethod
    def obtener_usuario_id(cls, cliente, id):
        bd_usuarios = os.getenv("BD_USUARIOS")
        usuario = cliente[bd_usuarios].find_one({"_id": id})
        return cls(**usuario) if usuario else None

    @classmethod
    def obtener_usuario_nombre_usuario(cls, cliente, nombre_usuario):
        bd_usuarios = os.getenv("BD_USUARIOS")
        usuario = cliente[bd_usuarios].find_one({"nombre_usuario": nombre_usuario})
        return cls(**usuario) if usuario else None

    # Metodos de instancia

    def actualizar_usuario(self, cliente, actualizacion):
        filtro = {"_id": self._id}
        bd_usuarios = os.getenv("BD_USUARIOS")
        cliente[bd_usuarios].update_one(filtro, actualizacion)

    def validar_credenciales(self, contrasena):
        return bcrypt.checkpw(contrasena.encode('utf-8'), self.contrasena)

    def obtener_configuracion_usuario(self):
        return self.configuracion_usuario
