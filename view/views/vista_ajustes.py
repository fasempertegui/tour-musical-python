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
        self.boton_establecer_ubicacion = ctk.CTkButton(self, text="Establecer ubicacion", command=self._establecer_ubicacion, **self.default_button_color)
        self.boton_establecer_ubicacion.pack_configure(**self.default_padding)
        self.boton_establecer_ubicacion.pack()

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()

    def _establecer_ubicacion(self, *args):
        dialog = ctk.CTkInputDialog(text="Ingresa las coordenadas:", title="Establecer ubicacion")
        coordenadas = dialog.get_input()
        if coordenadas is not None:
            if "," in coordenadas:
                self.controlador.establecer_ubicacion(coordenadas)
