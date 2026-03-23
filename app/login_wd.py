import os
import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3
from app.database import Database
from app.menu import Menu

'''###########################--JANELA LOGIN--#################################'''

class Login:
    def __init__(self, parent):
        self.janela = parent
    def login(self):
        self.janela_login = Toplevel(self.janela) # abrindo a tela de login em uma janela menor
        self.db = Database()
        self.janela_login.title("LOGIN") #titulo
        icon3 = PhotoImage(file="assets/icons/icone2.png")
        self.janela_login.iconphoto(False, icon3) #mudando o icone
        self.janela_login.resizable(False, False)
        self.janela_login.geometry("300x180+500+200") #tamanho e posição da janela
        frame_login = Frame(self.janela_login)
        usuario = Label(frame_login, text="Usuário: ", font="sylfaen 15 bold") #etiqueta que mostra onde inserir o usuario
        usuario.grid(row=0, sticky=W)
        senha = Label(frame_login, text="Senha: ", font="sylfaen 15 bold")  #etiqueta que mostra onde inserir a senha
        senha.grid(row=1, sticky=W)
        insert_usuario = Entry(frame_login)
        insert_usuario.grid(row=0, column=1, columnspan=2)
        insert_senha = Entry(frame_login, show='*')
        insert_senha.grid(row=1, column=1)
        confirmar = Button(frame_login, text="acessar", bd=5, cursor='hand2', relief="raised", bg='#B0E0E6', font="sylfaen 15 bold",
                           command= lambda: self.validacao(insert_usuario.get(), insert_senha.get()))
        self.mensagem = Label(frame_login, text='')
        self.mensagem.grid(row=2,columnspan=2)
        confirmar.grid(row=3, column=1, columnspan=2)
        self.janela_login.bind('<Return>', lambda event: self.validacao(insert_usuario.get(), insert_senha.get())) #ao pressionar enter tentar validar
        self.janela_login.bind('<Escape>', lambda event: self.janela_login.destroy()) #ao pressionar esc fecha a janela
        frame_login.grid(row=0, column=0, sticky="nsew")
        self.janela_login.grab_set()
        self.janela_login.focus_set()
        insert_usuario.focus()  # para iniciar com entry usuario
        self.janela_login.transient(self.janela)

    def validacao(self, user, senha): #metodo para verificar se a senha e usuario estão corretos
        query = 'SELECT * FROM Usuarios WHERE usuario = ? and senha = ?'
        parametros = user, senha

        teste1 = self.db.query(query, parametros)
        resposta = teste1.fetchall()

        if len(resposta) != 0:
            self.janela_login.destroy()
            self.janela.destroy()
            menu = Menu(self.janela)
            menu.pack(fill='both', expand=True)
        else:
            self.mensagem['text'] = 'Usuario ou senhas incorreto'''