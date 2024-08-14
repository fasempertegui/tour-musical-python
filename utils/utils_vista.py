import customtkinter as ctk


class VistaUtils:
    padding = {"padx": 10, "pady": 5}
    estilo_boton = {"fg_color": "#A1A892", "hover_color": "#9ca686", "text_color": "#2F242C", "text_color_disabled": "#737373"}

    @classmethod
    def crear_titulo(cls, contenedor, texto_titulo):
        estilo_titulo = {"size": 18, "weight": "bold"}
        estilo_titulo = ctk.CTkFont(**estilo_titulo)
        titulo_label = ctk.CTkLabel(contenedor, font=estilo_titulo)
        titulo_label.configure(text=texto_titulo)
        titulo_label.pack_configure(side="top", **cls.padding)
        return titulo_label

    @classmethod
    def crear_boton_atras(cls, contenedor):
        pack_config = {"side": "bottom", **VistaUtils.padding}
        boton_atras = ctk.CTkButton(contenedor, text="Volver", **cls.estilo_boton)
        boton_atras.pack_configure(**pack_config)
        return boton_atras
