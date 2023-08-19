import customtkinter as ctk


class VistaPrincipal(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.controlador = controlador

        self.default_padding = {"padx": 10, "pady": 5}
        self.default_button_color = {"fg_color": "#A1A892", "hover_color": "#9ca686", "text_color": "#2F242C", "text_color_disabled": "#737373"}

        titulo_fuente = ctk.CTkFont(size=18, weight="bold")
        self.titulo_label = ctk.CTkLabel(self, font=titulo_fuente)
        
        self.boton_atras = ctk.CTkButton(self, text="Volver", command=self.regresar, **self.default_button_color)
        

    def regresar(self):
        self.controlador.regresar()