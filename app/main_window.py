import os
import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3
from app.database import Database
from app.login_wd import Login
from app.sign_up_wd import Sign_up

'''################## CLASSE Window/ JANELA INICIAL ###################################################'''

class Window:
    ##db_auto = 'database/ManagerLuxury.db'# variavel para acessar o banco de dados
    def __init__(self, root): #construtor recebe a rota
        self.db = Database()
        self.janela = root #janela inicial vai receber root
        self.janela.title("Sistema de Gerenciamento de Frota Luxury Wheels")  # Adicionando um titulo a janela principal do programa
        self.janela.geometry(f"900x600+200+50")  # redimensionando o tamanho e posição da janela do programa de acordo com o tamanho da tela
        caminho_icone = os.path.join("assets", "icons", "icone1.png")
        icone = PhotoImage(file=caminho_icone)
        self.janela.iconphoto(False, icone)  # alterando o icone da janela
        self.janela['bg'] = '#B0E0E6' #alterando a cor de fundo da janela inicial
        #criando frame inicial com botão de login e exit
        self.janela.resizable(0,0) # impedir que a janela seja aumentada

        self.frame_inicial = Frame(self.janela) #Criando o frame inicial que vai receber a tela para login ou sair
        self.frame = LabelFrame(self.frame_inicial, text="Sistema de Gerenciamento de Frota Luxury Wheels", bd=8,
                                relief="groove", font="sylfaen 15 bold", bg="#E6E6FA") #frame com login ou sair
        self.login_button = Button(self.frame, text="Login", cursor='hand2', font="sylfaen 15 bold", bd=5, relief="raised",
                            bg='#B0E0E6', command=lambda: Login(self.janela).login()) #criando botão de login que vai abrir a janela para inserir os dados de autenticação
        self.login_button.grid(row=0, column=0, pady=20, padx=200) #posicionando botão login
        self.cadastrar = Button(self.frame, text="Cadastrar usuário", cursor='hand2', font="sylfaen 15 bold",
                                bd=5, relief="raised", bg='#B0E0E6', command=lambda: Sign_up(self.janela).cadastrar())
        self.cadastrar.grid(row=1, column=0)
        self.exit = Button(self.frame, text="Sair", cursor='hand2', font="sylfaen 15 bold", bd=5, relief="raised",
                           bg='#B0E0E6', command=self.exit) #criando botão de sair
        self.exit.grid(row=2, column=0, pady= 20) #posicionando botão de sair
        self.frame.grid(pady=200, padx=200) #posicionando frame
        self.login_button.focus_set()
        self.janela.bind('<Escape>', lambda event: self.janela.destroy())
        self.janela.bind('<Return>', self.enter_pressed)
        self.frame_inicial.grid() #posicionado frame inicial

    def exit(self): #metodo para encerrar o programa
        self.janela.destroy()

    def enter_pressed(self, event):
        widget = self.janela.focus_get()
        if isinstance(widget, Button):
            widget.invoke()
