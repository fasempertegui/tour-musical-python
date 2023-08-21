from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk


class VistaReviews(VistaPrincipal):
    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Reviews de usuarios")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        self.frame_reviews = ctk.CTkFrame(self, fg_color="transparent")

        self.texto = ctk.CTkTextbox(self.frame_reviews)
        self.texto.pack_configure(**self.default_padding, fill="both", expand=True)
        self.texto.pack()

        self.frame_reviews.pack_configure(fill="both", expand=True)
        self.frame_reviews.pack()

        self.master.bind("<<IrReviews>>", self.recuperar_reviews)

        self.boton_atras.pack(side='bottom', **self.default_padding)

    def recuperar_reviews(self, *args):
        # Habilito la edicion del widget de texto
        self.texto.configure(state="normal")
        # Borro el contenido del widget de texto
        self.texto.delete("1.0", tk.END)
        texto = self.controlador.recuperar_reviews()
        self.texto.insert(tk.END, texto)
        # Deshabilito la edicion del widget de texto   
        self.texto.configure(state="disabled")