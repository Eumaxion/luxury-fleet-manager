from src.modules import *
from src.main_window import Window

class Exit_page(Frame):
    def __init__(self, root, app):
        super().__init__()
        self.root = root
        self.app = app
        self.quit_exit()

    def quit_exit(self):
        #ABA PARA VOLTAR A TELA DE LOGIN
        lb = LabelFrame(self, text="SAIR", font='sylfaen 12 bold')
        botao_sair2 = Button(lb, text="logout", font='sylfaen 12 bold', command=self.sair)
        quit_program = Button(lb, text="quit", font='sylfaen 12 bold', command=self.exit)
        botao_sair2.grid()
        quit_program.grid()
        lb.grid(pady=265, padx=252)
        self.place(relx=0.251, rely=0.005, relheight=0.99, relwidth=0.745)

    def sair(self):
        #destroir a frame atual e voltar a frame inicial de login
        self.destroy()
        
    def exit(self): #metodo para encerrar o programa
        self.root.destroy()