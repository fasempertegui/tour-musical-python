from utils.utils_vista import VistaUtils

import tkinter as tk
import customtkinter as ctk


class VistaReviews(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Tu ubicacion")
        self.titulo_label.pack()

        self.descripcion_review = ctk.CTkLabel(self)
        self.descripcion_review.pack_configure(**VistaUtils.padding)
        self.descripcion_review.pack()

        frame_reviews = ctk.CTkFrame(self, fg_color="transparent")

        self.texto = ctk.CTkTextbox(frame_reviews)
        self.texto.pack_configure(**VistaUtils.padding, fill="both", expand=True)
        self.texto.pack()

        frame_reviews.pack_configure(fill="both", expand=True)
        frame_reviews.pack()

        self._inicializar()

        self.boton_atras = VistaUtils.crear_boton_atras(self)
        self.boton_atras.configure(command=self.regresar)
        self.boton_atras.pack()

    def regresar(self):
        self.controlador.regresar()

    def _inicializar(self, *args):
        evento = self.controlador.obtener_evento_actual()
        texto_descripcion = f"{evento.nombre} por {evento.artista}"
        self.descripcion_review.configure(text=texto_descripcion)
        # Habilito la edicion del widget de texto
        self.texto.configure(state="normal")
        # Borro el contenido del widget de texto
        self.texto.delete("1.0", tk.END)
        texto_reviews = self.controlador.recuperar_reviews()
        self.texto.insert(tk.END, texto_reviews)
        # Deshabilito la edicion del widget de texto
        self.texto.configure(state="disabled")
