import customtkinter as ctk

from utils.utils_vista import VistaUtils


class VistaAjustes(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Tu ubicacion")
        self.titulo_label.pack()

        self.label_ubicacion = ctk.CTkLabel(self, text="Tu ubicacion")
        self.label_ubicacion.pack()

        self.boton_establecer_ubicacion = ctk.CTkButton(self, text="Establecer ubicacion", command=self.ir_a_ubicacion, **VistaUtils.estilo_boton)
        self.boton_establecer_ubicacion.pack_configure(**VistaUtils.padding)
        self.boton_establecer_ubicacion.pack()

        self.boton_atras = VistaUtils.crear_boton_atras(self)
        self.boton_atras.configure(command=self.regresar)
        self.boton_atras.pack()

    def regresar(self):
        self.controlador.regresar()

    def ir_a_ubicacion(self, *args):
        self.controlador.ir_a_ubicacion()
