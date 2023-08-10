import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaReviews(ttk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.master = master
        self.controlador = controlador

        titulo_fuente = Font(size=13, weight="bold")
        self.titulo = ttk.Label(
            self, text="Reviews de usuarios", font=titulo_fuente)
        self.titulo.pack(padx=10, pady=15)

        self.frame_reviews = ttk.Frame(self)

        hbar = tk.Scrollbar(self.frame_reviews, orient="horizontal")
        hbar.pack(side="bottom", fill="x")
        vbar = tk.Scrollbar(self.frame_reviews, orient="vertical")
        vbar.pack(side="right", fill="y")

        self.texto = tk.Text(self.frame_reviews, width=35, height=12, wrap='none', xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.texto.pack(side="top", fill="x")

        hbar.config(command=self.texto.xview)
        vbar.config(command=self.texto.yview)

        self.frame_reviews.pack()

        self.boton_atras = ttk.Button(
            self, text="Volver", command=self.regresar
        )
        self.boton_atras.pack(padx=10, pady=5)

    def _obtener_nombre_usuario(self, id_usuario):
        return self.controlador.obtener_nombre_usuario(id_usuario)

    def establecer_reviews(self, evento):
        # Habilito la edicion del widget de texto
        self.texto.config(state="normal")
        # Borro el contenido del widget de texto
        self.texto.delete("1.0", tk.END)
        reviews = self.obtener_reviews_evento(evento)
        for review in reviews:
            usuario = self._obtener_nombre_usuario(review.id_usuario)
            estrellas = ""
            for i in range(review.calificacion):
                estrellas += "⭐"
            texto = f"{usuario} ({estrellas}):\n{review.comentario}\n\n"
            self.texto.insert(tk.END, texto)
        # Deshabilito la edicion del widget de texto   
        self.texto.config(state="disabled")

    def obtener_reviews_evento(self, evento):
        return self.controlador.obtener_reviews_evento(evento)

    def regresar(self):
        self.controlador.regresar()