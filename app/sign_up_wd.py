import os
import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3
from app.database import Database

'''###########################--JANELA CADASTRO--#################################'''

class Sign_up:
    def __init__(self, parent):
        self.janela = parent
    def cadastrar(self):
        self.janela_cadastro = Toplevel(self.janela)
        self.db = Database()
        self.janela_cadastro.title("CADASTRAR USUARIO")  # titulo
        icon2 = PhotoImage(file="assets/icons/icone2.png")
        self.janela_cadastro.iconphoto(False, icon2)  # mudando o icone
        self.janela_cadastro.resizable(False, False)
        self.janela_cadastro.geometry("550x300+400+200")  # tamanho e posição da janela
        frame_cadastro = Frame(self.janela_cadastro)
        id_usuario = Label(frame_cadastro, text="Insira seu ID:", font="sylfaen 15 bold")
        self.insert_id = Entry(frame_cadastro, width=45)
        nome = Label(frame_cadastro, text="Insira nome: ", font="sylfaen 15 bold")
        self.insert_nome = Entry(frame_cadastro, width=45)
        usuario_lb = Label(frame_cadastro, text="Insira usuário: ", font="sylfaen 15 bold") #etiqueta que mostra onde inserir o usuario
        self.insert_usuario = Entry(frame_cadastro, width=45)
        label_senha = Label(frame_cadastro, text="Senha: ", font="sylfaen 15 bold")  #etiqueta que mostra onde inserir a senha
        self.insert_senha = Entry(frame_cadastro, width=45)
        info_senha = Label(frame_cadastro, text="A senha deve conter no minimo\n8 digitos com letras e numeros.", font="sylfaen 12 italic")
        self.mensagem_cadastro=Label(frame_cadastro, text='', font="sylfaen 13 bold", fg="red")
        button_insert = Button(frame_cadastro, text="Confirmar dados", cursor='hand2', font="sylfaen 13 bold",
                               command=lambda: self.verificar_cadastro(self.insert_id.get(), self.insert_usuario.get(), 
                               self.insert_senha.get(), self.insert_nome.get()))

        id_usuario.grid(row=0)      ######### Posicionando os widgets na frame.
        self.insert_id.grid(row=0, column=1)
        nome.grid(row=1)
        self.insert_nome.grid(row=1, column=1)
        usuario_lb.grid(row=2, column=0)
        self.insert_usuario.grid(row=2, column=1)
        label_senha.grid(row=3, column=0)
        self.insert_senha.grid(row=3, column=1)
        info_senha.grid(row=4, columnspan=3)
        button_insert.grid(row=5, rowspan=3, columnspan=3)
        self.mensagem_cadastro.grid(row=8, columnspan=3)
        frame_cadastro.pack()
        self.janela_cadastro.bind('<Escape>', lambda event: self.janela_cadastro.destroy())
        self.janela_cadastro.bind('<Return>', lambda event: self.verificar_cadastro(self.insert_id.get(), 
                                self.insert_usuario.get(), self.insert_senha.get(), self.insert_nome.get()))
        self.janela_cadastro.grab_set()
        #self.janela_cadastro.focus_set()
        self.janela_cadastro.transient(self.janela)
        self.insert_id.focus()

    def verificar_cadastro(self, id, usuario, senha, nome):
        self.mensagem_cadastro['text'] = ''     #Limpando a mensagem
        senha_pequena = len(senha) < 8  #testando se a senha é menor que oito digitos
        senha_letras = senha.isalpha() #testando se a senha não tem numeros
        senha_numeros = senha.isnumeric() #testando se a senha não tem letras
        campos = [
        id,
        usuario,
        senha,
        nome
         ]
        if any(campo.strip() == "" for campo in campos):  # Verificando se algum campo está vazio
            self.mensagem_cadastro['text'] = "Preencha todos os campos!"
            return
        if senha_pequena:       #fazendo os testes e retornando erro.
            self.mensagem_cadastro['text'] = 'A senha deve conter no minimo 8 letras.'
            return
        elif senha_letras:
            self.mensagem_cadastro['text'] = 'A senha deve conter pelo menos um numero.'
            return
        elif senha_numeros:
            self.mensagem_cadastro['text'] = 'A senha deve conter pelo menos uma letra.'
            return
        else:
            return self.inserir_usuario(id, usuario, senha, nome)
            # se tudo estiver de acordo é chamada a função de inserir_usuario

    def inserir_usuario(self, id, usuario, senha, nome):
        query_id = "SELECT * FROM usuarios WHERE ID = ? OR usuario = ?"
        parametros1 = id, usuario
        consulta = self.db.query(query_id, parametros1)
        resposta = consulta.fetchall()
        if id.isdigit():
            try:
                if int(id) == resposta[0][0]:
                    self.mensagem_cadastro['text'] = 'O colaborador com o ID informado\n já está cadastrado.'
                    return
                elif usuario == resposta[0][1]:
                    self.mensagem_cadastro['text'] = 'O nome de usuario informado\n já está sendo utulizado.'
                return
            except IndexError as i:
                query2 = "INSERT INTO usuarios VALUES(?,?,?,?)"
                paramentros2 = id, usuario, senha, nome
                self.db.query(query2, paramentros2)
                self.mensagem_cadastro['text'] = 'Usuário cadastrado com sucesso!'
                self.insert_id.delete(0, 'end')
                self.insert_nome.delete(0, 'end')
                self.insert_senha.delete(0, 'end')
                self.insert_usuario.delete(0, 'end')
                self.insert_id.focus()
                return
        else:
            self.mensagem_cadastro['text'] = 'Campo ID aceita apenas numeros'
