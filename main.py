import customtkinter as ctk
from dotenv import load_dotenv

from controller.controllers.controlador_login import ControladorLogin
from controller.controllers.controlador_inicio import ControladorInicio
from view.views.vista_login import VistaLogin
from view.views.vista_inicio import VistaInicio

from database.database import Conexion
from auth.sesion import Sesion


class Aplicacion(ctk.CTk):

    def __init__(self):
        super().__init__()

        load_dotenv()

        conexion = Conexion()
        self.cliente = conexion.obtener_cliente()

        self.title("Tour musical")
        self.geometry("450x450")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        if self._validar_sesion():
            self.ir_a_inicio()
        else:
            self._limpiar_sesion()
            self.ir_a_login()

        self.bind("<<logout>>", self.ir_a_login)

    def _validar_sesion(self):
        return Sesion.validar_sesion(self.cliente)

    def _limpiar_sesion(self):
        Sesion.eliminar_sesion(self.cliente)

    def ir_a_login(self, *args):
        self.historial_vistas = []
        controlador_login = ControladorLogin(self)
        self.vista_login = VistaLogin(self, controlador_login)
        self.cambiar_frame(self.vista_login)

    def ir_a_inicio(self, *args):
        self.historial_vistas = []
        controlador_inicio = ControladorInicio(self)
        vista_inicio = VistaInicio(self, controlador_inicio)
        self.cambiar_frame(vista_inicio)

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
