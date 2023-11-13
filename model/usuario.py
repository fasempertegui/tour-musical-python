class Usuario:

    def __init__(self, _id, nombre_usuario, contrasena, historial_eventos):
        self._id = _id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.historial_eventos = historial_eventos

    @classmethod
    def obtener_usuarios(cls, cliente):
        coleccion = cliente["usuarios"]
        data = list(coleccion.find())
        return [cls(**usuario) for usuario in data]

    @classmethod
    def obtener_usuario_id(cls, cliente, id):
        coleccion = cliente["usuarios"]
        usuario = coleccion.find_one({"_id": id})
        return cls(**usuario)
    
    @classmethod
    def obtener_usuario_nombre_usuario(cls, cliente, nombre_usuario):
        coleccion = cliente["usuarios"]
        usuario = coleccion.find_one({"nombre_usuario": nombre_usuario})
        if usuario is not None:
            return cls(**usuario)
        else:
            return usuario

    def validar_credenciales(self, usuario, contrasena):
        return self.nombre_usuario == usuario and self.contrasena == contrasena

class Sesion:

    usuario_actual = None

    @classmethod
    def autenticar_usuario(cls, cliente, nombre_usuario, contrasena):
        usuarios = Usuario.obtener_usuarios(cliente)
        for usuario in usuarios:
            if usuario.validar_credenciales(nombre_usuario, contrasena):
                cls.usuario_actual = usuario
                return True
        return False

    def _generar_id(cliente):
        usuarios = Usuario.obtener_usuarios(cliente)
        if len(usuarios) > 0:
            id_generada = usuarios[-1]._id + 1
        else:
            id_generada = 1000
        return id_generada

    @classmethod
    def registrar_usuario(cls, cliente, nombre_usuario, contrasena):
        id_generada = cls._generar_id(cliente)
        nuevo_usuario = Usuario(id_generada, nombre_usuario, contrasena, [])
        coleccion = cliente["usuarios"]
        coleccion.insert_one(nuevo_usuario.__dict__)
        cls.usuario_actual = nuevo_usuario

    @classmethod
    def actualizar_eventos_asistidos(cls, cliente, id_evento):
        usuario_actual = cls.obtener_usuario_actual()
        usuario_actual.historial_eventos.append(id_evento)
        filtro = {"_id": usuario_actual._id}
        actualizacion = {"$set": {"historial_eventos": usuario_actual.historial_eventos}}
        coleccion = cliente["usuarios"]
        coleccion.update_one(filtro, actualizacion)

    @classmethod
    def cerrar_sesion(cls):
        cls.usuario_actual = None

    @classmethod
    def obtener_usuario_actual(cls):
        return cls.usuario_actual
