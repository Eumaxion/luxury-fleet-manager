from src.modules import *
from src.pages.exit_page import Exit_page
from src.pages.legalize import Legalize
from src.pages.vehicles import Veiculos
from src.pages.maintence import Maintence

'''################################################# CLASSE MENU ###################################################'''
class Menu_Frame(Frame):
    def __init__(self):
        super().__init__()
        self.menu_page()

    def menu_page (self):
        self.frame_principal = Frame(self.master, highlightbackground='black', highlightthickness=2, bg="#AC4E0F")
        self.frame_esquerdo = Frame(self.frame_principal, highlightbackground='black', highlightthickness=2, bg='#6AE298')
        #self.frame_direito = Frame(self.frame_principal, highlightbackground='black', highlightthickness=2, bg='#6AE298')
        self['bd'] = 2 #defininado o tamanho da borda
        self['relief'] = SOLID #definindo o tipo
        # frame que vai estar os botões e os indicadores
        self.frame = Frame(self.frame_esquerdo, bg="#6AE298", highlightbackground='black', highlightthickness=2)
        # criando os botões para as abas e seus respectivos indicadores!
        b_veic_disp = Button(self.frame, text="VEICULOS", cursor='hand2', font="sylfaen 13 bold", bd=0, background="#6AE298",
                             command=lambda: self.indicar(self.indicador_disponiveis, Veiculos()))
        self.indicador_disponiveis = Label(self.frame, text='', bg="#E26A6A")
        b_legalizar = Button(self.frame, text="LEGALIZAR", cursor='hand2', font="sylfaen 13 bold", bd=0, background="#6AE298",
                             command=lambda: self.indicar(self.indicador_legalizar, Legalize()))
        self.indicador_legalizar = Label(self.frame, text='', bg="#6AE298")
        b_manutencao = Button(self.frame, text="MANUTENÇÃO", cursor='hand2', font="sylfaen 13 bold", bd=0, background="#6AE298",
                              command=lambda: self.indicar(self.indicador_manutencao, Maintence()))
        self.indicador_manutencao = Label(self.frame, text='', bg="#6AE298")
        b_sair = Button(self.frame, text="SAIR", cursor='hand2', font="sylfaen 13 bold", bd=0, background="#6AE298",
                        command=lambda: self.indicar(self.indicador_sair, Exit_page()))
        self.indicador_sair = Label(self.frame, text='', bg="#6AE298")
        # Posicionando os botões, indicadores e as frames
        self.frame_principal.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.frame_esquerdo.place(relx=0, rely=0, relheight=1, relwidth=0.25)
        self.frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        b_veic_disp.place(x=50, y=100)  #
        self.indicador_disponiveis.place(x=10, y=90, width=10, height=60)
        b_legalizar.place(x=50, y=200)
        self.indicador_legalizar.place(x=10, y=190, width=10, height=60)
        b_manutencao.place(x=50, y=300)
        self.indicador_manutencao.place(x=10, y=290, width=10, height=60)
        b_sair.place(x=50, y=400)
        self.indicador_sair.place(x=10, y=390, width=10, height=60)
        self.start_frame()

    def delet_page(self, frame_atual):
        #DELETAR A FRAME ATUAL PARA POSICIONAR A NOVA FRAME QUE FOR CLICADA
        for item in frame_atual.winfo_children():
            item.destroy()

    def remover_indicador(self):
        #TIRAR A MARCAÇÃO DOS INDICADORE (ALTERAR A COR)
        self.indicador_disponiveis.config(bg='#6AE298')
        self.indicador_sair.config(bg='#6AE298')
        self.indicador_manutencao.config(bg='#6AE298')
        self.indicador_legalizar.config(bg='#6AE298')

    def indicar(self, indicador, novo_frame):
        #MOTRAR O INDICADOR QUE FOI CLICADO, DELETAR A FRAME ATUAL E INSERIR OS DADOS DA FRAME INDICADA.
        self.remover_indicador()
        indicador.config(bg='red')
        self.trocar_frame(novo_frame)

    def trocar_frame(self, novo_frame):
        if self.frame_atual is not None:
            self.frame_atual.destroy()
        self.frame_atual = novo_frame
        self.frame_atual.place()

    def start_frame(self):
        self.frame_atual = Veiculos()
        self.frame_atual.place()

    def mostrar_menu(self):
        self.trocar_frame(Menu)