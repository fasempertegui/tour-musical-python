class Usuario:

    usuarios = []

    def __init__(self, _id, nombre_usuario, contrasena, historial_eventos):
        self._id = _id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.historial_eventos = historial_eventos

    @classmethod
    def cargar_usuarios(cls, cliente):
        coleccion = cliente["usuarios"]
        data = list(coleccion.find())
        cls.usuarios = [cls(**usuario) for usuario in data]

    def verificar_contrasena(self, contrasena):
        return self.contrasena == contrasena

    # Getters

    @classmethod
    def obtener_usuarios(cls):
        return cls.usuarios

    @classmethod
    def obtener_usuario_id(cls, id):
        return next((usuario for usuario in cls.usuarios if usuario._id == id), None)

    @classmethod
    def obtener_usuarios_evento(cls, id_evento):
        return list(usuario for usuario in cls.usuarios if id_evento in usuario.historial_eventos)


class Sesion:

    usuario_actual = None

    @classmethod
    def autenticar(cls, nombre_usuario, contrasena):
        for usuario in Usuario.obtener_usuarios():
            if usuario.nombre_usuario == nombre_usuario and usuario.verificar_contrasena(contrasena):
                cls.usuario_actual = usuario
                return True
        return False

    @classmethod
    def actualizar_eventos_asistidos(cls, cliente, id_evento):
        cls.obtener_usuario_actual().historial_eventos.append(id_evento)
        filtro = {"_id": cls.obtener_usuario_actual()._id}
        actualizacion = {"$set": {"historial_eventos": cls.obtener_usuario_actual().historial_eventos}}
        coleccion = cliente["usuarios"]
        coleccion.update_one(filtro, actualizacion)

    @classmethod
    def cerrar_sesion(cls):
        cls.usuario_actual = None

    @classmethod
    def obtener_usuario_actual(cls):
        return cls.usuario_actual
