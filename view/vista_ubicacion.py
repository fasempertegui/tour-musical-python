import customtkinter as ctk
from tkintermapview import TkinterMapView

from utils.utils_vista import VistaUtils


class VistaUbicacion(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Tu ubicacion")
        self.titulo_label.pack()

        label = ctk.CTkLabel(self, text="Clic derecho para establecer tu ubicacion")
        label.pack()

        self.mapa = TkinterMapView(self, corner_radius=0)
        self.mapa.pack(padx=10, pady=10, fill="both", expand=True)
        self.mapa.add_right_click_menu_command(label="Estoy aqui", command=self.anadir_marcador, pass_coords=True)
        self.mapa.set_position(-24.78076361883803, -65.415784358493)
        self.mapa.set_zoom(15)

        frame_botones = ctk.CTkFrame(self, fg_color="transparent")
        frame_botones.rowconfigure(0, weight=1)
        frame_botones.columnconfigure(0, weight=1)
        frame_botones.pack_configure(side='bottom')
        frame_botones.pack()

        boton_aceptar = ctk.CTkButton(frame_botones, text="Aceptar", command=self.guardar_cambios, **VistaUtils.estilo_boton)
        boton_aceptar.grid_configure(row=0, column=0, padx=5, pady=10)
        boton_aceptar.grid()

        boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=self.regresar, **VistaUtils.estilo_boton)
        boton_cancelar.grid_configure(row=0, column=1, padx=5, pady=10)
        boton_cancelar.grid()

    def anadir_marcador(self, coordenadas):
        self.mapa.delete_all_marker()
        self.mapa.set_marker(coordenadas[0], coordenadas[1], text="Tu ubicacion")
        self.controlador.establecer_coordenadas(coordenadas)

    def guardar_cambios(self):
        if self.controlador.obtener_coordenadas():
            self.controlador.guardar_cambios()
        self.controlador.regresar()

    def regresar(self):
        self.controlador.regresar()
