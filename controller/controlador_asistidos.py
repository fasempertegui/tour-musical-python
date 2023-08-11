from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorAsistidos(ControladorPrincipalEventos):
    def __init__(self, app):
        super().__init__(app)
        # Lista de eventos propia de la subclase
        self.lista_eventos_asistidos = []
        self._lista_eventos_asistidos()

    def _lista_eventos_asistidos(self):
        historial_eventos_usuario = self.app.usuario_logueado.historial_eventos
        for id in historial_eventos_usuario:
            for evento in self.app.lista_eventos:
                if evento.id == id:
                    self.lista_eventos_asistidos.append(evento)
                    break
    
    # Implementacion propia de la subclase
    def obtener_eventos(self):
        return self.lista_eventos_asistidos