import os
import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3
from app.database import Database
from app.menu import Menu

def page_sair(self):
    #ABA PARA VOLTAR A TELA DE LOGIN
    teste = Frame(self.frame2)
    lb = LabelFrame(teste, text="SAIR", font='sylfaen 12 bold')
    botao_sair2 = Button(lb, text="Voltar ao menu inicial", font='sylfaen 12 bold', command=self.sair)
    quit_program = Button(lb, text="Sair do programa", font='sylfaen 12 bold', command=self.exit)
    botao_sair2.grid()
    quit_program.grid()
    lb.grid(pady=265, padx=252)
    teste.pack()
def sair(self):
    #destroir a frame atual e voltar a frame inicial de login
    self.destroy()
    from app.main_window import Window
    Window(self.master)
def exit(self): #metodo para encerrar o programa
    self.master.destroy()