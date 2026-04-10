from src.modules import *
from src.login_window import Window

class Exit_page(Frame):
    def __init__(self):
        super().__init__()
        self.quit_exit()

    def quit_exit(self):
        #ABA PARA VOLTAR A TELA DE LOGIN
        lb = LabelFrame(self, text="SAIR", font='sylfaen 12 bold')
        b_logout = Button(lb, text="logout", font='sylfaen 12 bold', command= lambda : self.logout(self.root))
        quit_program = Button(lb, text="quit", font='sylfaen 12 bold', command= lambda : self.exit())
        b_logout.grid()
        quit_program.grid()
        lb.grid(pady=265, padx=252)
        self.place(relx=0.251, rely=0.005, relheight=0.99, relwidth=0.745)

    def logout(self, root):
        #destroir a frame atual e voltar a frame inicial de login
        for item in self.winfo_children():
            item.destroy()
        self.frame_atual = Window(root, self)
        self.frame_atual.place()
        
    def exit(self): #metodo para encerrar o programa
        for item in self.master.winfo_children():
            item.destroy()
        self.master.destroy()