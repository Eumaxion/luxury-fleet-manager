from src.modules import *

root = Tk()

class App:
    ##db_auto = 'database/ManagerLuxury.db'# variavel para acessar o banco de dados
    def __init__(self): #construtor recebe a rota
        self.root = root
        self.front()
        self.frame_atual = None
        self.start_window()
        root.mainloop() 

    def front(self):
        self.root.title("Sistema de Gerenciamento de Frota Luxury Wheels")
        self.caminho_icone = os.path.join("assets", "icons", "icone1.png")
        self.icone = PhotoImage(file=self.caminho_icone)
        self.root.iconphoto(False, self.icone)  # alterando o icone da janela
        self.root.configure(background="#743913")
        self.root.geometry(f"900x600+200+50")
        self.root.maxsize(width=900, height=900)
        self.root.minsize(width=600, height=600)
        self.root.bind('<Escape>', lambda event: self.exit())
        self.root.bind('<Return>', self.enter_pressed)
    
    def exit(self): #metodo para encerrar o programa
        self.root.destroy()

    def enter_pressed(self, event):
        widget = self.root.focus_get()
        if isinstance(widget, Button):
            widget.invoke()

    def trocar_frame(self, novo_frame):
        if self.frame_atual is not None:
            self.frame_atual.destroy()  # apaga tela atual
        self.frame_atual = novo_frame(self.root)
        self.frame_atual.place()

    def start_window(self):
        self.frame_atual = Menu(self.root, self)
        self.frame_atual.place()

    def mostrar_menu(self):
        self.trocar_frame(Menu)

App()