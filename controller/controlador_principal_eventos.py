'''

Al igual que con las vistas, controlador_eventos, controlador_busqueda y controlador_asistidos comparten varios metodos, por lo que tambien implemente una clase padre

'''

from datetime import datetime


class ControladorPrincipalEventos:
    def __init__(self, app, lista_eventos, lista_ubicaciones):
        self.app = app
        self.lista_ubicaciones = lista_ubicaciones
        # lista_eventos contiene todos los eventos cargados desde data/eventos.json y no se modifica.
        self.lista_eventos = lista_eventos
        self.lista_eventos_proximos = []
        self.lista_eventos_finalizados = []
        self._separar_eventos()

    def _separar_eventos(self):
        hoy = datetime.now().replace(microsecond=0).isoformat()
        for evento in self.lista_eventos:
            if evento.hora_inicio > hoy:
                self.lista_eventos_proximos.append(evento)
            else:
                self.lista_eventos_finalizados.append(evento)

    # Metodo "privado" utilizado por las subclases.
    def _seleccionar_evento(self, indice, lista):
        if indice is not None:
            evento = lista[indice]
            for ubicacion in self.lista_ubicaciones:
                if ubicacion.id == evento.id_ubicacion:
                    ubicacion_evento = ubicacion
                    break
            if evento in self.lista_eventos_proximos:
                self.app.vista_info_proximos.establecer_info_evento(evento, ubicacion_evento)
                self.app.vista_mapa.agregar_marcador(ubicacion_evento)
                self.app.cambiar_frame(self.app.vista_info_proximos)
            else:
                self.app.vista_info_finalizados.establecer_info_evento(evento)
                self.app.vista_info_finalizados.determinar_usuario_asistio(evento)
                self.app.vista_reviews.establecer_reviews(evento)
                self.app.cambiar_frame(self.app.vista_info_finalizados)
    
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