import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaInicio(ttk.Frame):

    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        fuente_titulo = Font(size=16, weight="bold")
        self.titulo = ttk.Label(
            self, text="Bienvenido a Tour Musical", font=fuente_titulo)
        self.titulo.pack(padx=10, pady=15)

        fuente_descripcion = Font(size=12)
        self.descripcion = ttk.Label(
            self, text="Descubre eventos musicales, planifica rutas y comparte tu experiencia de manera eficiente y agradable con esta app", font=fuente_descripcion, wraplength=250)
        self.descripcion.pack(padx=10, pady=15)

        self.frame_botones = ttk.Frame(self)

        self.boton_explorar = ttk.Button(
            self.frame_botones, text="Explorar eventos", command=self.mostrar_eventos)
        self.boton_explorar.grid(row=0, column=0, pady=5)

        self.boton_buscar = ttk.Button(
            self.frame_botones, text="Buscar eventos", command=self.busqueda)
        self.boton_buscar.grid(row=1, column=0, pady=5)

        self.boton_asistidos = ttk.Button(
            self.frame_botones, text="Eventos asistidos", command=self.eventos_asistidos)
        self.boton_asistidos.grid(row=2, column=0, pady=5)

        self.frame_botones.pack(padx=10, pady=15)

    def mostrar_eventos(self):
        self.controlador.mostrar_eventos()

    def busqueda(self):
        self.controlador.busqueda()

    def eventos_asistidos(self):
        self.controlador.eventos_asistidos()