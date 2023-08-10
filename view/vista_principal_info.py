import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


'''

vista_principal_info y sus subclases comparten widgets (y algunos metodos tambien) por lo que decidi tambien implementar una clase padre

'''


class VistaPrincipalInfo(ttk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.master = master
        self.controlador = controlador

        titulo_fuente = Font(size=13, weight="bold")
        self.titulo_label = ttk.Label(self, text="", font=titulo_fuente)
        self.titulo_label.pack(padx=10, pady=5)

        descripcion_fuente = Font(size=10)
        self.descripcion_label = ttk.Label(
            self, text="", font=descripcion_fuente, wraplength=250)
        self.descripcion_label.pack(pady=5)

        self.info_evento_label = ttk.Label(self, text="")
        self.info_evento_label.pack(padx=10, pady=5)

        self.boton_atras = ttk.Button(
            self, text="Volver", command=self.regresar
        )

        # El boton para regresar se packea al final de cada subclase


    # mostrar_info_evento se implementa en cada subclase ya que cada una recibe diferente cantidad de argumentos

    def regresar(self):
        self.controlador.regresar()
