from app.modules import *

'''################## CLASSE Window/ JANELA INICIAL ###################################################'''

class Window(Frame):
    ##db_auto = 'database/ManagerLuxury.db'# variavel para acessar o banco de dados
    def __init__(self, root): #construtor recebe a rota
        super().__init__()
        self.root = root
        self.db = Database()
        self.frame_inicial = Frame(self.root, bd=4, bg='#743913', highlightthickness=3)
        self.frame = LabelFrame(self.frame_inicial, text="  Sistema de Gerenciamento de Frota Luxury Wheels ", bd=8,
                                relief="groove", font="sylfaen 15 bold", bg="#E6E6FA") #frame com login ou sair
        self.login_button = Button(self.frame, text="Login", cursor='hand2', font="sylfaen 15 bold", bd=5, relief="raised",
                            bg='#743913', command=lambda: Login(self.root).login()) #criando botão de login que vai abrir a janela para inserir os dados de autenticação
        self.cadastrar = Button(self.frame, text="Cadastrar usuário", cursor='hand2', font="sylfaen 15 bold",
                                bd=5, relief="raised", bg='#743913', command=lambda: Sign_up(self.root).cadastrar())
        self.exit_button = Button(self.frame, text="Sair", cursor='hand2', font="sylfaen 15 bold", bd=5, relief="raised",
                           bg='#743913', command=lambda: self.root.destroy()) #criando botão de sair
        self.login_button.focus_set()

        self.frame_inicial.place(relx=0.21, rely=0.2, relheight=0.5, relwidth=0.62)
        self.frame.place(relx=0, rely=0, relheight=1, relwidth=1)#posicionando frame
        self.login_button.place(relx=0.4, rely=0.1) #posicionando botão login
        self.cadastrar.place(relx=0.3, rely=0.35)
        self.exit_button.place(relx=0.41, rely=0.6) #posicionando botão de sair
