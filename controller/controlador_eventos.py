'''

Al igual que con las vistas, controlador_eventos, controlador_busqueda y controlador_asistidos comparten varios metodos, por lo que tambien implemente una clase padre

'''

from datetime import datetime


class ControladorEventos:
    def __init__(self, app, lista_eventos, lista_ubicaciones):
        self.app = app
        self.lista_eventos = lista_eventos
        self.lista_ubicaciones = lista_ubicaciones
        self.lista_eventos_proximos = []
        self.lista_eventos_finalizados = []
        self._separar_eventos()
        
    def _separar_eventos(self):
        hoy = datetime.now().replace(microsecond=0).isoformat()
        for evento in self.obtener_eventos():
            if evento.hora_inicio > hoy:
                self.lista_eventos_proximos.append(evento)
            else:
                self.lista_eventos_finalizados.append(evento)

    def seleccionar_evento(self, evento):
        if evento is not None:
            for ubicacion in self.obtener_ubicaciones():
                if ubicacion.id == evento.id_ubicacion:
                    ubicacion_evento = ubicacion
                    break
            if evento in self.obtener_eventos_proximos():
                self.app.vista_proximos.set_evento(evento, ubicacion_evento)
                self.app.vista_mapa.set_ubicacion(ubicacion_evento)
                self.app.cambiar_frame(self.app.vista_proximos)
            else:
                self.app.vista_finalizados.set_evento(evento)
                self.app.vista_reviews.set_evento(evento)
                self.app.cambiar_frame(self.app.vista_finalizados)
    
    def obtener_eventos(self):
        return self.lista_eventos

    def obtener_eventos_proximos(self):
        return self.lista_eventos_proximos

    def obtener_eventos_finalizados(self):
        return self.lista_eventos_finalizados

    def obtener_ubicaciones(self):
        return self.lista_ubicaciones

    def regresar(self):
        self.app.volver_frame_anterior()