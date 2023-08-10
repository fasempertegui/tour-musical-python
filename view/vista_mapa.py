import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView


class VistaMapa(ttk.Frame):

    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.master = master
        self.controlador = controlador

        frame_mapa = ttk.Frame(self)
        frame_mapa.pack(padx=10, pady=5)
        self.mapa = TkinterMapView(frame_mapa, width=270, height=270, corner_radius=1)
        self.mapa.pack(padx=10, pady=5)

        boton_atras = ttk.Button(self, text="Volver", command=self.regresar)
        boton_atras.pack(padx=10, pady=5)

    def agregar_marcador(self, ubicacion):
        latitud, longitud = ubicacion.coordenadas.split(",")
        self.mapa.set_position(float(latitud), float(longitud))
        self.mapa.set_marker(float(latitud), float(longitud))
        self.mapa.set_zoom(15)

    def regresar(self):
        self.controlador.regresar()