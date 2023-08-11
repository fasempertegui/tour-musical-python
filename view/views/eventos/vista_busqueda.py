from view.views.vista_eventos import VistaEventos

import tkinter as tk
from tkinter import ttk


class VistaBusqueda(VistaEventos):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label["text"] = "Buscar eventos"
        self.titulo_label.pack(**self.default_padding)

        label_frame = ttk.LabelFrame(self)
        label_frame["text"] = "Buscar por"

        OPCIONES = [
            "Nombre",
            "Artista",
            "Genero"
        ]

        # Con value=OPCIONES[0] la primera opcion (nombre) estara marcada por default
        self.opcion_elegida = tk.StringVar(value=OPCIONES[0])

        # Crear los radio buttons de manera dinamica
        for index, opcion in enumerate(OPCIONES):
            ttk.Radiobutton(
                label_frame,
                text=opcion,
                value=opcion,
                variable=self.opcion_elegida,
                command=self.actualizar_eventos
            ).grid(row=0, column=index, padx=3, pady=3)

        label_frame.pack()

        frame_entry_box = ttk.Frame(self)

        self.entry_box = ttk.Entry(frame_entry_box)
        # Placeholder para el campo de busqueda
        self.entry_box.insert(0, "Buscar")
        # Limpiar el campo cuando se hace focus en el
        self.entry_box.bind("<FocusIn>", self.limpiar_campo)
        self.entry_box.pack(side='left', padx=5)

        boton_busqueda = ttk.Button(
            frame_entry_box,
            text="Buscar",
            command=self.buscar_eventos
        )
        boton_busqueda.pack(side='right', padx=5)

        frame_entry_box.pack(pady=5)

        # Listbox en la clase padre
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)
        self.listbox.pack(**self.default_padding, fill="both", expand="true")

        self.actualizar_eventos()

        # Boton en la clase padre, padre
        self.boton_atras.pack(side='bottom', **self.default_padding)

    def seleccionar_evento(self, event):
        lista = self.obtener_eventos_buscados()
        indice = self.obtener_evento_seleccionado()
        evento = lista[indice]
        self.controlador.seleccionar_evento(evento)

    def buscar_eventos(self):
        criterio = self.opcion_elegida.get().lower()
        texto_busqueda = self.entry_box.get().lower()
        # Filtra la lista de todos los eventos
        eventos_filtrados = self.controlador.buscar_eventos(criterio, texto_busqueda)
        # Actualiza la listbox con los resultados de la busqueda
        self.listbox.delete(0, tk.END)
        for evento in eventos_filtrados:
            self.listbox.insert(tk.END, evento.nombre)

    # Elimina cualquier texto que pueda contener el campo (placeholder o texto ingresado)
    def limpiar_campo(self, *args):
        self.entry_box.delete(0, "end")

    def obtener_eventos_buscados(self):
        return self.controlador.obtener_eventos_buscados()