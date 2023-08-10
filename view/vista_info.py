import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaInfo(ttk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.master = master
        self.controlador = controlador
        
        titulo_fuente = Font(size=13, weight="bold")
        self.titulo_label = ttk.Label(self, text="", font=titulo_fuente)
        self.titulo_label.pack(padx=10, pady=5)

        descripcion_fuente = Font(size=10)
        self.descripcion_label = ttk.Label(self, text="", font=descripcion_fuente, wraplength=250)
        self.descripcion_label.pack(pady=5)

        self.info_evento_label = ttk.Label(self, text="")
        self.info_evento_label.pack(padx=10, pady=5)

        nombre_ubicacion_fuente = Font(size=9, weight="bold")        
        self.nombre_ubicacion_label = ttk.Label(self, text="", font=nombre_ubicacion_fuente)
        self.nombre_ubicacion_label.pack()

        self.direccion_ubicacion_label = ttk.Label(self, text="")
        self.direccion_ubicacion_label.pack()

        self.boton_ver_mapa = ttk.Button(
            self,
            text="Ver en mapa",
            command=self.ver_mapa)
        self.boton_ver_mapa.pack(padx=10, pady=5)

        self.boton_atras = ttk.Button(
            self, text="Volver", command=self.regresar
        )
        self.boton_atras.pack(padx=10, pady=5)
        
    def mostrar_info_evento(self, evento, ubicacion):
        nombre_ubicacion = ubicacion.nombre
        direccion_ubicacion = ubicacion.direccion
        self.titulo_label["text"] = evento.nombre
        self.descripcion_label["text"] = evento.descripcion
        self.nombre_ubicacion_label["text"] = nombre_ubicacion
        self.direccion_ubicacion_label["text"] = direccion_ubicacion
        (fecha, hora_inicio) = evento.hora_inicio.split("T")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label["text"] = info

    def ver_mapa(self):
        self.controlador.ver_mapa()

    def regresar(self):
        self.controlador.regresar()