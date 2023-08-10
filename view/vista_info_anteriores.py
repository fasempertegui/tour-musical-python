import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from view.vista_principal_info import VistaPrincipalInfo


class VistaInfoAnteriores(VistaPrincipalInfo):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.master = master

        self.frame_reviews = ttk.Frame(self)

        self.boton_ver_reviews = ttk.Button(
            self.frame_reviews, text="Ver reviews")
        self.boton_ver_reviews.pack(side='left')

        self.boton_escribir_review = ttk.Button(
            self.frame_reviews, text="Escribir review")
        self.boton_escribir_review.configure(state="disabled")
        self.boton_escribir_review.pack(side='right')

        self.frame_reviews.pack()

        self.boton_atras.pack(padx=10, pady=5)

    def mostrar_info_evento(self, evento):
        self.titulo_label["text"] = evento.nombre
        self.descripcion_label["text"] = evento.descripcion
        (fecha, hora_inicio) = evento.hora_inicio.split("T")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label["text"] = info
