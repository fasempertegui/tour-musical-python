from view.views.vista_info_evento import VistaInfoEvento

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaProximos(VistaInfoEvento):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        nombre_ubicacion_fuente = Font(size=9, weight="bold")
        self.nombre_ubicacion_label = ttk.Label(self, font=nombre_ubicacion_fuente)
        self.nombre_ubicacion_label.pack()

        self.direccion_ubicacion_label = ttk.Label(self)
        self.direccion_ubicacion_label.pack()

        boton_ver_mapa = ttk.Button(self, text="Ver en mapa", command=self.ir_a_mapa)
        boton_ver_mapa.pack(**self.default_padding)
        
        # Boton en la clase padre, padre
        self.boton_atras.pack(side='bottom', **self.default_padding)

    def _establecer_info_evento(self, evento, ubicacion):
        nombre_ubicacion = ubicacion.nombre
        direccion_ubicacion = ubicacion.direccion
        self.titulo_label["text"] = evento.nombre
        self.descripcion_label["text"] = evento.descripcion
        self.nombre_ubicacion_label["text"] = nombre_ubicacion
        self.direccion_ubicacion_label["text"] = direccion_ubicacion
        (fecha, hora_inicio) = evento.hora_inicio.split("T")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label["text"] = info

    def set_evento(self, evento, ubicacion):
        self._establecer_info_evento(evento, ubicacion)

    def ir_a_mapa(self):
        self.controlador.ir_a_mapa()