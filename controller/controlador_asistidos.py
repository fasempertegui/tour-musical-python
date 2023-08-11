from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorAsistidos(ControladorPrincipalEventos):
    def __init__(self, app, lista_eventos, lista_ubicaciones, usuario_logueado):
        super().__init__(app, lista_eventos, lista_ubicaciones)
        self.usuario_logueado = usuario_logueado
        # Lista de eventos propia
        self.lista_eventos_asistidos = []
        self._lista_eventos_asistidos()

    def _lista_eventos_asistidos(self):
        historial_eventos_usuario = self.usuario_logueado.historial_eventos
        for id in historial_eventos_usuario:
            for evento in self.lista_eventos:
                if evento.id == id:
                    self.lista_eventos_asistidos.append(evento)
                    break

    # Implementacion propia
    def obtener_eventos(self):
        return self.lista_eventos_asistidos
