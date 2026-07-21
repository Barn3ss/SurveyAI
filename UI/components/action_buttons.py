import customtkinter as ctk


class ActionButtons:

    def __init__(

        self,

        master,

        generar_callback,

        prompts_callback

    ):

        self.boton_generar = ctk.CTkButton(

            master,

            text="🚀 Generar encuesta",

            command=generar_callback,

            height=50

        )

        self.boton_generar.pack(

            fill="x",

            padx=25,

            pady=20

        )

        self.prompts = ctk.CTkButton(

            master,

            text="🛠 Editar prompts",

            command=prompts_callback,

            fg_color="gray30"

        )

        self.prompts.pack(
            pady=10
        )
        