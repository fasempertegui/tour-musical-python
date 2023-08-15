from view.views.vista_eventos import VistaEventos

import tkinter as tk
from tkinter import ttk


class VistaExplorar(VistaEventos):
    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label["text"] = "Explorar eventos"
        self.titulo_label.pack(**self.default_padding)

        label_frame = ttk.LabelFrame(self)
        label_frame["text"] = "Mostrar"

        OPCIONES = [
            "Todos",
            "Eventos proximos",
            "Eventos finalizados"
        ]

        # Con value=0 la primera opcion (todos) estara marcada por default
        self.opcion_elegida = tk.IntVar(value=0)

        # Crear los radio buttons de manera dinamica
        for index, opcion in enumerate(OPCIONES):
            ttk.Radiobutton(
                label_frame,
                text=opcion,
                value=index,
                variable=self.opcion_elegida,
                command=self.cambiar_lista
            ).grid(row=0, column=index, padx=3, pady=3)

        label_frame.pack()

        # Boton en la clase padre, padre
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)
        self.listbox.pack(**self.default_padding, fill="both", expand="true")

        self.actualizar_eventos()

        # Boton en la clase padre
        self.boton_atras.pack(side='bottom', **self.default_padding)

    def cambiar_lista(self):
        opcion = self.opcion_elegida.get()
        eventos = self.controlador.cambiar_lista(opcion)
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def seleccionar_evento(self, event):
        opcion = self.opcion_elegida.get()
        lista = self.controlador.cambiar_lista(opcion)
        indice = self.obtener_evento_seleccionado()
        evento = lista[indice]
        self.controlador.seleccionar_evento(evento)