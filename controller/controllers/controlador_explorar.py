from controller.controllers.controlador_eventos import ControladorEventos


class ControladorExplorar(ControladorEventos):
    def __init__(self, app, **datos):
        super().__init__(app, **datos)

    def cambiar_lista(self, opcion):
        match opcion:
            case 1:
                eventos = self.obtener_eventos_proximos()
            case 2:
                eventos = self.obtener_eventos_finalizados()
            case _:
                eventos = self.obtener_eventos()
        return eventos