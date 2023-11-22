from view.vista_principal import VistaPrincipal
import customtkinter as ctk

class VistaAjustes(VistaPrincipal):
    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.titulo_label.configure(text="Ajustes")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        self.label_ubicacion = ctk.CTkLabel(self, text="Tu ubicacion")
        self.label_ubicacion.pack()
        self.boton_establecer_ubicacion = ctk.CTkButton(self, text="Establecer ubicacion", command=self._ir_a_ubicacion, **self.default_button_color)
        self.boton_establecer_ubicacion.pack_configure(**self.default_padding)
        self.boton_establecer_ubicacion.pack()

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()

    def _ir_a_ubicacion(self, *args):
        self.controlador.ir_a_ubicacion()