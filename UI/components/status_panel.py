import customtkinter as ctk

from UI.styles import *


class StatusPanel(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=CORNER_RADIUS
        )

        self.pack(fill="x", padx=25, pady=10)

        self.barra = ctk.CTkProgressBar(
            self,
            width=500
        )

        self.barra.pack(
            padx=20,
            pady=(20,10)
        )

        self.barra.set(0)

        self.estado = ctk.CTkLabel(
            self,
            text="⏳ Esperando briefing..."
        )

        self.estado.pack(
            pady=(0,20)
        )
    def actualizar_estado(self, texto):

        self.estado.configure(
            text=f"Estado: {texto}"
        )


    def actualizar_progreso(self, valor):

        self.barra.set(valor/100)

        