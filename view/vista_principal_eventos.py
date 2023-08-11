import tkinter as tk
from tkinter import ttk

'''

vista_eventos, vista_busqueda y vista_asistidos comparten algunos métodos por lo que me parecio conveniente implementar una clase padre

'''


class VistaPrincipalEventos(ttk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.master = master
        self.controlador = controlador

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

        self.boton_atras = ttk.Button(self, text="Volver", command=self.regresar)

    def actualizar_eventos(self):
        eventos = self.obtener_eventos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def obtener_evento_seleccionado(self):
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def obtener_eventos(self):
        return self.controlador.obtener_eventos()
    
    def regresar(self):
        self.controlador.regresar()