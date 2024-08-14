import customtkinter as ctk
from dotenv import load_dotenv

from auth.sesion import Sesion

from controller.controlador_finalizados import ControladorFinalizados
from controller.controlador_futuros import ControladorFuturos
from controller.controlador_login import ControladorLogin
from controller.controlador_inicio import ControladorInicio

from view.vista_finalizados import VistaFinalizados
from view.vista_futuros import VistaFuturos
from view.vista_login import VistaLogin
from view.vista_inicio import VistaInicio

from database.database import Conexion

# Agregar controles:
# click en aceptar cuando no se selecciono ninguna

# Agregar:
# roles
# usuario puede eliminar sus reviews


class Aplicacion(ctk.CTk):
    def __init__(self):
        super().__init__()

        load_dotenv()
        self.cliente = self._obtener_cliente()

        self.title("Tour musical")
        self.geometry("450x450")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        if Sesion.validar_sesion(self.cliente):
            self.ir_a_inicio()
        else:
            self.ir_a_login()

    # Publicos

    '''Para evitar el circular import'''

    def ir_a_login(self):
        self._inicializar_historial_vistas()
        self.cambiar_vista(ControladorLogin, VistaLogin)

    def ir_a_inicio(self):
        self._inicializar_historial_vistas()
        self.cambiar_vista(ControladorInicio, VistaInicio)

    def ir_a_futuros(self, evento, ubicacion):
        self.cambiar_vista(ControladorFuturos, VistaFuturos, evento, ubicacion)

    def ir_a_finalizados(self, evento):
        self.cambiar_vista(ControladorFinalizados, VistaFinalizados, evento)

    '''Estos metodos deben centralizarse aqui'''

    def cambiar_vista(self, controlador_cls, vista_cls, *args, **kwargs):
        controlador = controlador_cls(self, *args, **kwargs)
        vista = vista_cls(self, controlador)
        if vista not in self.historial_vistas:
            self.historial_vistas.append(vista)
        vista.grid(row=0, column=0, sticky='nsew')
        vista.tkraise()

    def volver_vista_anterior(self):
        if len(self.historial_vistas) > 1:
            self.historial_vistas.pop()
            vista_anterior = self.historial_vistas[-1]
            vista_anterior.tkraise()

    # Privados

    @staticmethod
    def _obtener_cliente():
        return Conexion().obtener_cliente()

    def _inicializar_historial_vistas(self):
        self.historial_vistas = []


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()


@staticmethod
def obtener_seleccion(listbox):
    indice = listbox.curselection()
    return indice[0] if indice else None
