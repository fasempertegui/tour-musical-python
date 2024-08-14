from utils.utils_vista import VistaUtils

import tkinter as tk
import customtkinter as ctk


class VistaEscribirReview(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Tu ubicacion")
        self.titulo_label.pack()

        self.descripcion_review = ctk.CTkLabel(self)
        self.descripcion_review.pack_configure(**VistaUtils.padding)
        self.descripcion_review.pack()

        frame_calificacion = ctk.CTkFrame(self, fg_color="transparent")
        frame_calificacion.pack()

        label_calificacion = ctk.CTkLabel(frame_calificacion, text="Calificacion")
        label_calificacion.pack_configure(side="top")
        label_calificacion.pack()

        OPCIONES = [
            "1 ⭐",
            "2 ⭐",
            "3 ⭐",
            "4 ⭐",
            "5 ⭐"
        ]

        self.option_menu = ctk.CTkOptionMenu(frame_calificacion, values=OPCIONES)
        self.option_menu.set(OPCIONES[0])
        self.option_menu.pack_configure(**VistaUtils.padding)
        self.option_menu.pack()

        frame_comentario = ctk.CTkFrame(self, fg_color="transparent")
        frame_comentario.pack_configure(fill="both", expand=True)
        frame_comentario.pack()

        self.label_comentario = ctk.CTkLabel(frame_comentario, text="Comentario")
        self.label_comentario.pack_configure(side="top")
        self.label_comentario.pack()

        self.textbox = ctk.CTkTextbox(frame_comentario)
        self.textbox.pack_configure(fill="both", expand=True, padx=10)
        self.textbox.pack()

        self.boton_enviar = ctk.CTkButton(frame_comentario, text="Enviar review", command=self._enviar_review, **VistaUtils.estilo_boton)
        self.boton_enviar.pack_configure(side="bottom", **VistaUtils.padding)
        self.boton_enviar.pack()

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

    def _enviar_review(self):
        calificacion = int(self.option_menu.get().split(" ")[0])
        comentario = self.textbox.get("1.0", tk.END).strip()
        self.controlador.enviar_review(calificacion, comentario)
        self.controlador.regresar()
