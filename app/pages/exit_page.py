from tkinter import *

class ExitPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        Label(self, text="SAIR", font="sylfaen 16 bold").pack(pady=20)

        Button(self, text="Voltar", command=self.voltar).pack(pady=10)
        Button(self, text="Sair", command=self.sair).pack(pady=10)

    def voltar(self):
        self.destroy()

    def sair(self):
        self.winfo_toplevel().destroy()