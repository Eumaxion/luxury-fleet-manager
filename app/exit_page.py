from tkinter import ttk
from tkinter import *

class Exit_page:
    def __init__(self, parent):
        self.parent = parent

    def quit_exit(self):
        #ABA PARA VOLTAR A TELA DE LOGIN
        teste = Frame(self.parent)
        lb = LabelFrame(teste, text="SAIR", font='sylfaen 12 bold')
        botao_sair2 = Button(lb, text="Voltar ao menu inicial", font='sylfaen 12 bold', command=self.sair)
        quit_program = Button(lb, text="Sair do programa", font='sylfaen 12 bold', command=self.exit)
        botao_sair2.grid()
        quit_program.grid()
        lb.grid(pady=265, padx=252)
        teste.pack()
    def sair(self):
        #destroir a frame atual e voltar a frame inicial de login
        self.parent.destroy()
        from app.main_window import Window
        root = Tk()
        Window(root)
        root.mainloop()
    def exit(self): #metodo para encerrar o programa
        self.parent.destroy()