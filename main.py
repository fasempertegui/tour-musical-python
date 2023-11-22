from controller.controllers.controlador_login import ControladorLogin 
from view.views.vista_login import VistaLogin

from database.database import Conexion

from dotenv import load_dotenv

import customtkinter as ctk

class Aplicacion(ctk.CTk):

    def __init__(self):

        load_dotenv()

        conexion = Conexion()
        self.cliente = conexion.obtener_cliente()

        ctk.CTk.__init__(self)
        ctk.set_appearance_mode("Light")
        self.title("Tour musical")
        self.geometry("450x450")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.inicializar()

        self.bind("<<logout>>", self.inicializar)

    def inicializar(self, *args):
        self.historial_vistas = []

        controlador_login = ControladorLogin(self)
        self.vista_login = VistaLogin(self, controlador_login)
        
        self.cambiar_frame(self.vista_login)

    def cambiar_frame(self, frame_destino):
        if frame_destino not in self.historial_vistas:
            self.historial_vistas.append(frame_destino)
        frame_destino.grid(row=0, column=0, sticky='nsew')
        frame_destino.tkraise()

    def volver_frame_anterior(self):
        if len(self.historial_vistas) > 1:
            self.historial_vistas.pop()
            vista_anterior = self.historial_vistas[-1]
            self.cambiar_frame(vista_anterior)


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()