import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaInicio(ttk.Frame):

    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        fuente_titulo = Font(size=16, weight="bold")
        titulo = ttk.Label(self, text="Bienvenido a Tour Musical", font=fuente_titulo)
        titulo.pack(padx=10, pady=15)

        fuente_descripcion = Font(size=12)
        descripcion = ttk.Label(self, text="Descubre eventos musicales, planifica rutas y comparte tu experiencia de manera eficiente y agradable con esta app", font=fuente_descripcion, wraplength=250)
        descripcion.pack(padx=10, pady=15)

        frame_botones = ttk.Frame(self)

        boton_explorar = ttk.Button(frame_botones, text="Explorar eventos", command=self.mostrar_eventos)
        boton_explorar.grid(row=0, column=0, pady=5)

        boton_buscar = ttk.Button(frame_botones, text="Buscar eventos", command=self.busqueda)
        boton_buscar.grid(row=1, column=0, pady=5)

        boton_asistidos = ttk.Button(frame_botones, text="Eventos asistidos", command=self.eventos_asistidos)
        boton_asistidos.grid(row=2, column=0, pady=5)

        frame_botones.pack(padx=10, pady=15)

    def mostrar_eventos(self):
        self.controlador.mostrar_eventos()

    def busqueda(self):
        self.controlador.busqueda()

    def eventos_asistidos(self):
        self.controlador.eventos_asistidos()