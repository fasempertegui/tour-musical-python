from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk


class VistaFinalizados(VistaPrincipal):
    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        self.descripcion_label = ctk.CTkLabel(self, wraplength=250)
        self.descripcion_label.pack_configure(**self.default_padding)
        self.descripcion_label.pack()

        frame_info_evento = ctk.CTkFrame(self, fg_color="transparent")
        frame_info_evento.pack_configure(fill="both", expand=True)
        frame_info_evento.pack()

        self.info_evento_label = ctk.CTkLabel(frame_info_evento)
        self.info_evento_label.pack_configure(side="bottom", **self.default_padding)
        self.info_evento_label.pack()

        frame_principal_reviews = ctk.CTkFrame(self, fg_color="transparent")
        frame_principal_reviews.pack_configure(fill="both", expand=True)
        frame_principal_reviews.pack()

        frame_reviews = ctk.CTkFrame(frame_principal_reviews, fg_color="transparent")
        frame_reviews.pack_configure(side="bottom", **self.default_padding)
        frame_reviews.pack()

        estado_fuente = ctk.CTkFont(weight="bold")
        estado_label = ctk.CTkLabel(frame_reviews, text="Evento finalizado", font=estado_fuente)
        estado_label.pack_configure(side="top", **self.default_padding)
        estado_label.pack()

        frame_botones = ctk.CTkFrame(frame_reviews, fg_color="transparent")
        frame_botones.pack_configure(side="bottom")
        frame_botones.pack()

        self.boton_confirmar_asistencia = ctk.CTkButton(frame_botones, command=self._confirmar_asistencia, **self.default_button_color)
        self.boton_confirmar_asistencia.pack_configure(side="top", padx=3, pady=3)
        self.boton_confirmar_asistencia.pack()

        self.boton_ver_reviews = ctk.CTkButton(frame_botones, text="Ver reviews", command=self.ir_a_reviews, **self.default_button_color)
        self.boton_ver_reviews.pack_configure(side="left", padx=3, pady=3)
        self.boton_ver_reviews.pack()

        self.boton_escribir_review = ctk.CTkButton(frame_botones, text="Opinar", command=self.ir_a_escribir_review, **self.default_button_color)
        self.boton_escribir_review.pack_configure(side="right", padx=3, pady=3)
        self.boton_escribir_review.pack()

        self._inicializar()

        self.master.bind("<<inicializar_finalizados>>", self._inicializar)
        self.master.bind("<<actualizar_botones>>", self._inicializar)

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()

    def _establecer_info_evento(self):
        evento = self.controlador.obtener_evento_actual()
        self.titulo_label.configure(text=evento.nombre)
        self.descripcion_label.configure(text=evento.descripcion)
        fecha = evento.hora_inicio.date().strftime("%d-%m-%Y")
        hora_inicio = evento.hora_inicio.time().strftime("%H:%M:%S")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label.configure(text=info)

    def _inicializar(self, *args):
        self._establecer_info_evento()
        if self.controlador.determinar_usuario_asistio():
            self.boton_confirmar_asistencia.configure(
                state="disabled", text="Marcado como asistido")
            if self.controlador.determinar_usuario_puede_opinar():
                self.boton_escribir_review.configure(state="normal")
            else:
                self.boton_escribir_review.configure(state="disabled")
        else:
            self.boton_confirmar_asistencia.configure(
                state="normal", text="Marcar como asistido")
            self.boton_escribir_review.configure(state="disabled")

    def _confirmar_asistencia(self, *args):
        self.controlador.confirmar_asistencia()

    # Navegacion

    def ir_a_reviews(self):
        self.controlador.ir_a_reviews()

    def ir_a_escribir_review(self):
        self.controlador.ir_a_escribir_review()
