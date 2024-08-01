import os
from model.usuario import Usuario

class Sesion:

    usuario_actual = None

    @classmethod
    def autenticar_usuario(cls, cliente, nombre_usuario, contrasena):
        usuario = Usuario.obtener_usuario_nombre_usuario(cliente, nombre_usuario)
        if usuario and usuario.validar_credenciales(contrasena):
            cls.usuario_actual = usuario
            return True
        return False

    @classmethod
    def registrar_usuario(cls, cliente, nombre_usuario, contrasena):
        nuevo_usuario = Usuario.crear_usuario(cliente, nombre_usuario, contrasena)
        cls.usuario_actual = nuevo_usuario

    @classmethod
    def actualizar_eventos_asistidos(cls, cliente, id_evento):
        usuario_actual = cls.obtener_usuario_actual()
        if usuario_actual:
            usuario_actual.historial_eventos.append(id_evento)
            filtro = {"_id": usuario_actual._id}
            actualizacion = {"$set": {"historial_eventos": usuario_actual.historial_eventos}}
            coleccion = cliente[os.getenv("BD_USUARIOS")]
            coleccion.update_one(filtro, actualizacion)

    @classmethod
    def actualizar_configuracion_ubicacion(cls, cliente, coordenadas):
        usuario_actual = cls.obtener_usuario_actual()
        if usuario_actual:
            usuario_actual.configuracion_usuario = {"ubicacion": coordenadas}
            filtro = {"_id": usuario_actual._id}
            actualizacion = {"$set": {"configuracion_usuario": {"ubicacion": coordenadas}}}
            coleccion = cliente[os.getenv("BD_USUARIOS")]
            coleccion.update_one(filtro, actualizacion)

    @classmethod
    def cerrar_sesion(cls):
        cls.usuario_actual = None

    @classmethod
    def obtener_usuario_actual(cls):
        return cls.usuario_actual
