from view.vista_principal import VistaPrincipal

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaProximos(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.pack(**self.default_padding)

        descripcion_fuente = Font(size=10)
        self.descripcion_label = ttk.Label(self, font=descripcion_fuente, wraplength=250)
        self.descripcion_label.pack(**self.default_padding)

        self.info_evento_label = ttk.Label(self)
        self.info_evento_label.pack(**self.default_padding)

        nombre_ubicacion_fuente = Font(size=9, weight="bold")
        self.nombre_ubicacion_label = ttk.Label(self, font=nombre_ubicacion_fuente)
        self.nombre_ubicacion_label.pack()

        self.direccion_ubicacion_label = ttk.Label(self)
        self.direccion_ubicacion_label.pack()

        boton_ver_mapa = ttk.Button(self, text="Ver en mapa", command=self.ir_a_mapa)
        boton_ver_mapa.pack(**self.default_padding)

        self.master.bind("<<VistaProximos>>", self._inicializar)
        
        self.boton_atras.pack(side='bottom', **self.default_padding)

    def _establecer_info_evento(self):
        evento = self.controlador.obtener_evento_actual()
        ubicacion = self.controlador.obtener_ubicacion_actual()
        self.titulo_label["text"] = evento.nombre
        self.descripcion_label["text"] = evento.descripcion
        self.nombre_ubicacion_label["text"] = ubicacion.nombre
        self.direccion_ubicacion_label["text"] = ubicacion.direccion
        (fecha, hora_inicio) = evento.hora_inicio.split("T")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label["text"] = info

    def _inicializar(self, event):
        self._establecer_info_evento()
    
    # Navegacion

    def ir_a_mapa(self):
        self.controlador.ir_a_mapa()