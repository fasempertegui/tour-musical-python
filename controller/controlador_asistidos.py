from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorAsistidos(ControladorPrincipalEventos):
    def __init__(self, app, lista_eventos, lista_ubicaciones, usuario):
        super().__init__(app, lista_eventos, lista_ubicaciones)
        self.usuario = usuario
        # Lista de eventos propia de la subclase
        self.lista_eventos_asistidos = []
        self._lista_eventos_asistidos()

    def _lista_eventos_asistidos(self):
        for id in self.usuario.historial_eventos:
            for evento in self.lista_eventos:
                if evento.id == id:
                    self.lista_eventos_asistidos.append(evento)
                    break
    
    # Implementacion propia de la subclase
    def obtener_eventos(self):
        return self.lista_eventos_asistidos

    def seleccionar_evento(self, indice):
        lista = self.lista_eventos_asistidos
        self._seleccionar_evento(indice, lista)