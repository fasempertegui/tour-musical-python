import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from view.vista_principal_info import VistaPrincipalInfo


class VistaInfoFinalizados(VistaPrincipalInfo):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        frame_reviews = ttk.Frame(self)

        estado_fuente = Font(size=9, weight="bold")
        estado_label = ttk.Label(
            self, text="Evento finalizado", font=estado_fuente)
        estado_label.pack(padx=10, pady=5)

        self.boton_confirmar_asistencia = ttk.Button(
            frame_reviews, text="Asisti a este evento")
        self.boton_confirmar_asistencia.pack(side='top')

        self.boton_ver_reviews = ttk.Button(
            frame_reviews, text="Ver reviews", command=self.mostrar_reviews)
        self.boton_ver_reviews.pack(side="left")

        self.boton_escribir_review = ttk.Button(
            frame_reviews, text="Escribir review")
        self.boton_escribir_review.pack(side="right")

        frame_reviews.pack()

        self.boton_atras.pack(padx=10, pady=5)

    def establecer_info_evento(self, evento):
        self.titulo_label["text"] = evento.nombre
        self.descripcion_label["text"] = evento.descripcion
        (fecha, hora_inicio) = evento.hora_inicio.split("T")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label["text"] = info

    def _puede_escribir_review(self, evento):
        reviews_usuario = self.controlador.obtener_reviews_usuario()
        for review in reviews_usuario:
            if review.id_evento == evento.id:
                # Si estamos dentro del if es porque el usuario ya escribio una review para este evento
                # Se deshabilita el boton
                self.boton_escribir_review.configure(state="disabled")
                break
        # Si no escribio review, el boton queda habilitado

    def determinar_usuario_asistio(self, evento):
        # El comportamiento de los botones es el siguiente:
        # Por default se asume que el usuario no asistio al evento, por lo que el boton para confirmar la asistencia esta habilitado
        self.boton_confirmar_asistencia.configure(state="normal")
        # Como el usuario no asistio al evento, no puede escribir una review
        self.boton_escribir_review.configure(state="disabled")
        usuario = self.controlador.obtener_usuario_logueado()
        # Determinamos verdaderamente si el usuario asistio al evento
        for id_evento in usuario.historial_eventos:
            if id_evento == evento.id:
                # Si estamos dentro del if es porque el usuario asistio al evento
                # El boton se deshabilita puesto que no necesita re-confirmar la asistencia
                self.boton_confirmar_asistencia.configure(state="disabled")
                # Se habilita el boton de review a modo de estado inicial
                self.boton_escribir_review.configure(state="enabled")
                # Resta determinar si puede escribir una review o no, dependiendo si ya lo hizo anteriormente o no
                self._puede_escribir_review(evento)
                break

    def mostrar_reviews(self):
        self.controlador.mostrar_reviews()
