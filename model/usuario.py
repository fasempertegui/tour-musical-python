class Usuario:

    usuarios = []
    id_usuario_actual = None

    def __init__(self, _id, nombre_usuario, historial_eventos):
        self._id = _id
        self.nombre_usuario = nombre_usuario
        self.historial_eventos = historial_eventos

    @classmethod
    def cargar_usuarios(cls, cliente):
        coleccion = cliente["usuarios"]
        data = list(coleccion.find())
        cls.usuarios = [cls(**usuario) for usuario in data]
        cls.id_usuario_actual = cls.usuarios[0]._id

    @classmethod
    def actualizar_eventos_asistidos_usuario(cls, cliente, id_evento):
        cls.obtener_usuario_id(cls.id_usuario_actual).historial_eventos.append(id_evento)
        historial_eventos = cls.obtener_usuario_id(cls.id_usuario_actual).historial_eventos
        filtro = {"_id": cls.id_usuario_actual}
        actualizacion = {"$set": {"historial_eventos": historial_eventos}}
        coleccion = cliente["usuarios"]
        coleccion.update_one(filtro, actualizacion)

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
    
    @classmethod
    def obtener_id_usuario_actual(cls):
        return cls.id_usuario_actual