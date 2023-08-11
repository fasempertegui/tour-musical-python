from controller.controlador_principal_eventos import ControladorPrincipalEventos


class ControladorEventos(ControladorPrincipalEventos):
    def __init__(self, app, lista_eventos, lista_ubicaciones):
        super().__init__(app, lista_eventos, lista_ubicaciones)

    def determinar_eventos(self, opcion):
        match opcion:
            case 1:
                eventos = self.obtener_eventos_proximos()
            case 2:
                eventos = self.obtener_eventos_finalizados()
            case _:
                eventos = self.obtener_eventos()
        return eventos