import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from view.vista_principal_eventos import VistaPrincipalEventos


class VistaEventos(VistaPrincipalEventos):
    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.master = master

        titulo_fuente = Font(size=13, weight="bold")
        self.titulo = ttk.Label(
            self, text="Explorar eventos", font=titulo_fuente)
        self.titulo.pack(padx=10, pady=5)

        self.label_frame = ttk.LabelFrame(self)
        self.label_frame["text"] = "Mostrar"

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
                self.label_frame,
                text=opcion,
                value=index,
                variable=self.opcion_elegida,
                command=self.actualizar_eventos
            ).grid(row=0, column=index, padx=3, pady=3)

        self.label_frame.pack()

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)
        self.listbox.pack(padx=10, pady=15)

        self.listbox.pack()

        self.actualizar_eventos()

        self.boton_atras = ttk.Button(
            self, text="Volver", command=self.regresar
        )
        self.boton_atras.pack(padx=10, pady=5)

    # Metodo "privado" utilizado por actualizar_eventos y seleccionar_evento de esta subclase
    def _determinar_eventos(self):
        opcion = self.opcion_elegida.get()
        match opcion:
            case 1:
                return self.obtener_eventos_proximos()
            case 2:
                return self.obtener_eventos_finalizados()
            case _:
                return self.obtener_eventos()

    def actualizar_eventos(self):
        eventos = self._determinar_eventos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def seleccionar_evento(self, event):
        indice = self.obtener_evento_seleccionado()
        eventos = self._determinar_eventos()
        self.controlador.seleccionar_evento(indice, eventos)
