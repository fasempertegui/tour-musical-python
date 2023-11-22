from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk


class VistaReviews(VistaPrincipal):
    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Reviews de usuarios")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        self.descripcion_review = ctk.CTkLabel(self)
        self.descripcion_review.pack_configure(**self.default_padding)
        self.descripcion_review.pack()

        frame_reviews = ctk.CTkFrame(self, fg_color="transparent")

        self.texto = ctk.CTkTextbox(frame_reviews)
        self.texto.pack_configure(**self.default_padding, fill="both", expand=True)
        self.texto.pack()

        frame_reviews.pack_configure(fill="both", expand=True)
        frame_reviews.pack()

        self.master.bind("<<ir_reviews>>", self._inicializar)

        self.boton_atras.pack(side='bottom', **self.default_padding)

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