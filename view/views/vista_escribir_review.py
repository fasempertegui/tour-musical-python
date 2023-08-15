from view.vista_principal import VistaPrincipal

import tkinter as tk
from tkinter import ttk


class VistaEscribirReview(VistaPrincipal):

    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.titulo_label["text"] = "Escribir review"
        self.titulo_label.pack(**self.default_padding)

        label_frame = ttk.LabelFrame(self, text="Calificacion")

        OPCIONES = [
            "1",
            "2",
            "3",
            "4",
            "5"
        ]

        # Con value=0 la primera opcion (1) estara marcada por default
        self.opcion_elegida = tk.IntVar(value=0)

        # Crear los radio buttons de manera dinamica
        for index, opcion in enumerate(OPCIONES):
            ttk.Radiobutton(
                label_frame,
                text=opcion,
                value=index,
                variable=self.opcion_elegida
            ).grid(row=0, column=index, padx=3, pady=3)

        label_frame.pack(**self.default_padding)

        self.label_comentario = ttk.LabelFrame(self, text="Comentario")
        self.label_comentario.pack(**self.default_padding)

        self.comentario_text = tk.Text(self.label_comentario, width=30, height=8)
        self.comentario_text.pack(**self.default_padding)

        self.boton_enviar = ttk.Button(self, text="Enviar Review", command=self.enviar_review)
        self.boton_enviar.pack(**self.default_padding)

        self.boton_atras.pack(side='bottom', **self.default_padding)

    def ref_evento_actual(self, evento):
        self.controlador.ref_evento_actual(evento)
    
    def enviar_review(self):
        calificacion = self.opcion_elegida.get() + 1
        comentario = self.comentario_text.get("1.0", tk.END).strip()
        self.controlador.enviar_review(calificacion, comentario)