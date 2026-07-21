import customtkinter as ctk


class Footer(ctk.CTkLabel):

    def __init__(self, master):

        super().__init__(

            master,

            text="SurveyAI v1.0",

            text_color="gray"

        )

        self.pack(
            side="bottom",
            pady=15
        )
        