from app.modules import *

class Maintence(Frame):
    def manutencao_page(self):
        #ABA PARA MOSTRAR OS VEICULOS EM ALERTA DE MANUTENÇÃO
        manutencao = Frame(self.frame2)
        frame_manutencao = LabelFrame(manutencao, text="VEICULOS EM ALERTA:", font="sylfaen 16 bold")
        self.tv_manutencao = ttk.Treeview(frame_manutencao, columns=('id_veiculo', 'placa', 'status','ultima',
                                                                        'proxima', 'n_utilizacoes', 'dias'), height=13, show='headings')
        self.tv_manutencao.column('id_veiculo', minwidth=0, width=40)
        self.tv_manutencao.column('placa', minwidth=0, width=80)
        self.tv_manutencao.column('status', minwidth=0, width=100)
        self.tv_manutencao.column('ultima', minwidth=0, width=120)
        self.tv_manutencao.column('proxima', minwidth=0, width=100)
        self.tv_manutencao.column('n_utilizacoes', minwidth=0, width=80)
        self.tv_manutencao.column('dias', minwidth=0, width=100)
        self.tv_manutencao.heading('id_veiculo', text='ID')
        self.tv_manutencao.heading('placa', text='PLACA')
        self.tv_manutencao.heading('status', text='STATUS')
        self.tv_manutencao.heading('ultima', text='ULTIMA MAN.')
        self.tv_manutencao.heading('proxima', text='PRÓXIMA MAN.')
        self.tv_manutencao.heading('n_utilizacoes', text='UTILIZAÇÕES')
        self.tv_manutencao.heading('dias', text='PRÓXIMA MANUTENÇÃO EM')
        self.label_manutencao = Label(frame_manutencao, text='''Veiculos com 50 utilizações ou perto da data
            de manutenção ficarão em alerta até serem regularizados''', font='sylfaen 12 bold', fg='blue')

        self.tv_manutencao.grid(row=0)
        self.label_manutencao.grid(row=1)
        self.tabela_manutencao()

        ##--- FRAME QUE VAI RECEBER AS INFORMAÇÕES PARA INSERIR UMA MANUTENÇÃO ---#
        self.frame_att_manutencao = LabelFrame(frame_manutencao, text='Enviar para manutenção', font='sylfaen 12 bold' )
        self.lb_id_manut = Label(self.frame_att_manutencao, text="ID do veiculo:", font='sylfaen 12 bold')
        self.ent_id_veic = Entry(self.frame_att_manutencao)
        self.lb_dias_manut = Label(self.frame_att_manutencao, text="Dias em manutenção:", font='sylfaen 12 bold')
        self.ent_dias_manut = Entry(self.frame_att_manutencao)
        self.lb_detalhes_manut = Label(self.frame_att_manutencao, text="Detalhes da manutenção: ", font='sylfaen 12 bold')
        self.ent_detalhes = Entry(self.frame_att_manutencao)
        self.lb_data_inicio_manu = Label(self.frame_att_manutencao, text="Data de inicio\n da manutenção:", font='sylfaen 12 bold')
        self.ent_data_inicio = Entry(self.frame_att_manutencao)
        self.ent_data_inicio.insert(0,"DD/MM/AAAA")
        self.check_valor3 = IntVar()
        self.check_atual = Checkbutton(self.frame_att_manutencao, text="Data atual", font='sylfaen 10 bold', variable=self.check_valor3,
                                            offvalue=0, onvalue=1, command=self.data_atual_manutencao)

        self.mensagem_atualizar = Label(self.frame_att_manutencao, text='', font="sylfaen 12 bold", fg='red')
        self.btt_enviar_manutencao = Button(self.frame_att_manutencao, cursor='hand2', bd=5, relief="raised", bg='#743913',
                                text="Confirmar", font="sylfaen 12 bold", command=lambda: self.atualizar_manutencao
            (self.ent_id_veic.get(), self.ent_dias_manut.get(), self.ent_data_inicio.get(), self.ent_detalhes.get()))
        icone_pesquisa = tkinter.PhotoImage(file='assets/icons/magnifying_glass.png')
        self.buttom_pesquisar_manutencao = Button(self.frame_att_manutencao, cursor='hand2', text='Pesquisar\nveiculo', font="sylfaen 10 bold", image=icone_pesquisa,
                                        compound='left', background='#743913', command=self.pesquisar_manutencao)
        self.buttom_pesquisar_manutencao.image = icone_pesquisa

        #POSICIONANDO OS WIDGETS NA FRAME
        self.lb_id_manut.grid(row=0,column=0, sticky='w')
        self.ent_id_veic.grid(row=0,column=1, sticky='w')
        self.lb_dias_manut.grid(row=0,column=2, sticky='w')
        self.ent_dias_manut.grid(row=0,column=3, sticky='w')
        self.lb_data_inicio_manu.grid(row=1,column=0)
        self.ent_data_inicio.grid(row=1,column=1)
        self.check_atual.grid(row=1, column=2, sticky='w')
        self.lb_detalhes_manut.grid(row=2,column=0, columnspan=4, padx=10)
        self.ent_detalhes.grid(row=3,column=0,columnspan=4,rowspan=3, padx=10, sticky='we')
        self.buttom_pesquisar_manutencao.grid(row=1, column=3, rowspan=2, padx=5, sticky='e')
        self.mensagem_atualizar.grid(row=6,column=0, columnspan=4, sticky='we')
        self.btt_enviar_manutencao.grid(row=7, column=0, columnspan=4)
        self.frame_att_manutencao.grid(row=2,column=0,padx=53, sticky='we')
        frame_manutencao.grid(row=1, padx=20)
        manutencao.pack(expand=TRUE, fill=BOTH)

    def tabela_manutencao(self):
        # QUERY PARA POPULAR A TABELA DE VEICULOS EM ALERTA QUE PRECISAM DE MANUTENÇÃO
        self.tv_manutencao.delete(*self.tv_manutencao.get_children()) #excluindo tabelas ja existente
        data_atual = datetime.today()
        informacoes = []
        query_dados_manutencao = ('SELECT id_veiculo, placa, disponibilidade, ultima_manutencao, proxima_manutencao, utilizacoes '
                                    'FROM automoveis ORDER BY utilizacoes DESC')
        datas_proxima_manutencao = self.db_consulta(query_dados_manutencao)
        for item in datas_proxima_manutencao:
            data_proxima = datetime.strptime(item[4], "%d/%m/%Y")
            dias = data_proxima - data_atual
            if item[5] >= 50: #se o veiculo tiver 50 ou mais utilizações entrará em alerta
                item = list(item)
                item.append(dias.days + 1)
                informacoes.append(item)
            elif dias.days <= 10: #se o veiculo estiver a 10 dias de proximidade da data de manutenção entrará em alerta
                item = list(item)
                item.append(dias.days + 1)
                informacoes.append(item)
        for item in informacoes:
            id, placa, disponibilidade, ultima_m, proxi, utl, dias = item
            dias = "< 24 horas" if dias == 0 else (f"atrasado "
                    f"{- dias} dia") if dias == -1 else (f"atrasado "
                    f"{- dias} dias") if dias < -1 else (f"{dias}"
                    f" dia") if dias == 1 else f"{dias} dias"
            ultima_m = "sem registro" if ultima_m == None else ultima_m
            self.tv_manutencao.insert('', 'end', values= (id, placa, disponibilidade, ultima_m, proxi, utl, dias))

    def atualizar_manutencao(self,ent_id_veic, ent_dias_manut, dt_inicio, detalhes):
        #FUNÇÃO PARA FAZER A INSERÇÃO DE UMA NOVA MANUTENÇÃO
        #TESTES PARA VERIFICAR SE OS DADOS INFORMADOS ESTÃO CORRETOS
        self.mensagem_atualizar['text'] = "" #limpando campo de mensagem de erros
        id_vazia = True if ent_id_veic == '' else False #verificar se o id está vazio
        dias_vazia = True if ent_dias_manut == '' else False #verificar se os dias de manutenção está preenchido
        data_vazia = True if dt_inicio == '' else False #verificar se a data está preenchida
        padrao_data = r'\d{2}/\d{2}/\d{4}'
        padrao_data_manut = re.match(padrao_data, dt_inicio) #verificar se a data está no padrão correto

        if id_vazia:
            self.mensagem_atualizar['text'] = "Campo 'ID' obrigatório!"
            return
        if dias_vazia:
            self.mensagem_atualizar['text'] = "Campo 'Dias em manutenção' obrigatório!"
            return
        try:
            int(ent_dias_manut)
        except ValueError as e:
            self.mensagem_atualizar['text'] = "Campo 'Dias em manutenção' incorreto!"
            return
        if data_vazia:
            self.mensagem_atualizar['text'] = "Campo 'DATA' obrigatório!"
            return
        if not padrao_data_manut:
            self.mensagem_atualizar['text'] = "Data informada inválida!"
            return

        query_status = 'SELECT disponibilidade FROM automoveis WHERE id_veiculo = ?'
        parametros_status = [ent_id_veic] #VERIFICANDO SE O VEICULO ENCONTRA-SE DISPONIVEL!
        resultado_status = self.db_consulta(query_status, parametros_status)
        if resultado_status[0][0] == 'ocupado' or resultado_status[0][0] == 'em manutenção':
            self.mensagem_atualizar['text'] = "O veiculo não encontra-se disponivel!"
            return

        #INSERINDO NOVA MANUTENÇÃO
        query_update_manutencao = "INSERT INTO manutencao (veiculo, detalhes, data, duracao) VALUES (?,?,?,?)"
        parametros_update_manutencao = ent_id_veic, detalhes, dt_inicio, ent_dias_manut
        self.db_consulta(query_update_manutencao, parametros_update_manutencao)

        dt_inicio = datetime.strptime(dt_inicio, '%d/%m/%Y')
        ocupado_ate = dt_inicio + timedelta(int(ent_dias_manut))
        proxima_manu = ocupado_ate + timedelta(365)
        dt_inicio = dt_inicio.strftime('%d/%m/%Y')
        ocupado_ate = ocupado_ate.strftime('%d/%m/%Y')
        proxima_manu = proxima_manu.strftime('%d/%m/%Y')

        #ATUALIZANDO STATUS/DADOS NA BASE DE DADOS DOS VEICULOS
        query_update_veic = ("UPDATE automoveis SET disponibilidade = 'em manutencao', utilizacoes = 0, disponivel_em = ?,"
                                "ultima_manutencao = ?, proxima_manutencao = ? WHERE id_veiculo = ?")
        parametros_update_veic = ocupado_ate,dt_inicio,proxima_manu,ent_id_veic
        self.db_consulta(query_update_veic, parametros_update_veic)
        self.mensagem_atualizar['text'] = "Status atualizado com sucesso!"
        self.tabela_manutencao()

    def pesquisar_manutencao(self):
        #JANELA PARA PESQUISAR MANUTENÇÕES DOS VEICULOS
        self.janela_pesquisar_m = Toplevel()
        self.janela_pesquisar_m.title("Pesquisar manutenções") #titulo da janela
        icon_lupa = PhotoImage(file="assets/icons/lupa-1.png")
        self.janela_pesquisar_m.iconphoto(False, icon_lupa) #icone
        self.janela_pesquisar_m.resizable(False,False) #impedir que a janela seja redimensionada
        self.janela_pesquisar_m.geometry("600x300+500+200") #posicionamento e tamanho da janela

        #INSERINDO FRAME E WIDGETS NA JANELA DE PESQUISA
        self.frame_pesquisar_m = Frame(self.janela_pesquisar_m)
        self.lb_id_m = Label(self.frame_pesquisar_m, text="ID ou PLACA", font="sylfaen 10 bold" )
        self.lb_id_manutencao_m = Label(self.frame_pesquisar_m, text="ID manutenção", font="sylfaen 10 bold")
        self.ent_id_m = Entry(self.frame_pesquisar_m)
        self.ent_id_manutencao = Entry(self.frame_pesquisar_m)
        self.bttm_id_m = Button(self.frame_pesquisar_m, cursor='hand2',text="OK", font="sylfaen 10 bold", bd=5,
                                relief="raised", bg='#743913',
                                command= lambda: self.buscar_manutencoes(self.ent_id_m.get(), self.ent_id_manutencao.get()))
        self.mensagem_erro_m = Label(self.frame_pesquisar_m, text=" ", font="sylfaen 10 bold", fg='red')

        #INSERINDO TABELA QUE VAI RECEBER O RESULTADO NA JANELA DE PESQUISA
        self.tabela_pesquisa_m = ttk.Treeview(self.frame_pesquisar_m, columns=('id_veiculo', 'id_manutencao', 'placa',
                                                            'detalhes', 'data', 'duracao'), height=8, show='headings' )
        self.tabela_pesquisa_m.column('id_veiculo', minwidth=0, width=90)
        self.tabela_pesquisa_m.column('id_manutencao', minwidth=0,width=90)
        self.tabela_pesquisa_m.column('placa', minwidth=0, width=70)
        self.tabela_pesquisa_m.column('detalhes', minwidth=0, width=180)
        self.tabela_pesquisa_m.column('data', minwidth=0, width=90)
        self.tabela_pesquisa_m.column('duracao', minwidth=0, width=70)
        self.tabela_pesquisa_m.heading('id_veiculo', text='ID Veiculo')
        self.tabela_pesquisa_m.heading('id_manutencao', text='ID Manutencao')
        self.tabela_pesquisa_m.heading('placa', text='PLACA')
        self.tabela_pesquisa_m.heading('detalhes', text='detalhes')
        self.tabela_pesquisa_m.heading('data', text='INICIO')
        self.tabela_pesquisa_m.heading('duracao', text='Duração')
        self.lb_id_m.grid(row=0, column=0, padx=5, sticky='E')
        self.lb_id_manutencao_m.grid(row=1, column=0, padx=5, sticky='E')
        self.ent_id_m.grid(row=0, column=1, padx=5, sticky='WE')
        self.ent_id_manutencao.grid(row=1, column=1, padx=5, sticky='WE')

        self.bttm_id_m.grid(row=0, column=2, rowspan=2, padx=5, sticky='W')
        self.mensagem_erro_m.grid(row=2, column=0, columnspan=2)
        self.tabela_pesquisa_m.grid(row=3, columnspan=3)
        self.janela_pesquisar_m.bind('<Escape>', lambda event: self.janela_pesquisar_m.destroy())
        self.janela_pesquisar_m.bind('<Return>', lambda event: self.buscar_manutencoes(self.ent_id_m.get(), self.ent_id_manutencao.get()))
        self.janela_pesquisar_m.grab_set()
        self.ent_id_m.focus()
        self.frame_pesquisar_m.pack()

    def buscar_manutencoes(self, id_placa, id_m):
        #FUNÇÃO PARA BUSCAR O RESULTADO DA PESQUISA
        self.tabela_pesquisa_m.delete(*self.tabela_pesquisa_m.get_children()) #deletando tabela anteriores
        registros_db = []
        if len(id_placa) == 0 and len(id_m) == 0: #erro caso nenhum campo seja informado
            self.mensagem_erro_m['text'] = 'Inserir informação!'
            return

        if len(id_placa) != 0: #busca por PLACA ou ID do veiculo usando o left join caso ainda não haja manutenção para o veiculo informado
            query_pesquisa = ('SELECT id_veiculo, id_manutencao, placa, detalhes, data, duracao FROM automoveis '
                                'LEFT JOIN manutencao ON automoveis.id_veiculo = manutencao.veiculo WHERE id_veiculo = ? OR placa = ?')
            id_placa = id_placa.upper()
            id_parametro = id_placa, id_placa
            registros_db = self.db_consulta(query_pesquisa, id_parametro)
            if registros_db == []: #mensagem de erro caso a placa ou ID não pertença a nenhum veiculo
                self.mensagem_erro_m['text'] = 'Não há veiculo com os dados informados!'
                return

        elif len(id_m) != 0: #busca por ID de manutenção usando o left join caso ainda não haja manutenção para o veiculo informado
            query_pesquisa = ('SELECT id_veiculo, id_manutencao, placa, detalhes, data, duracao FROM automoveis '
                                'LEFT JOIN manutencao ON automoveis.id_veiculo = manutencao.veiculo WHERE id_manutencao = ?')
            id_parametro = [id_m]
            registros_db = self.db_consulta(query_pesquisa, id_parametro)
            if registros_db == []:
                self.mensagem_erro_m['text'] = 'Manutenção não encontrada!'
                return

        self.mensagem_erro_m['text'] = ''
        for item in registros_db:
            id_veiculo, id_manutencao, placa, detalhes, data, duracao = item
            id_manutencao = '' if id_manutencao == None else id_manutencao
            detalhes = 'SEM REGISTROS ANTERIORES' if detalhes == None else detalhes
            duracao = '' if duracao == None else f" {duracao} dia" if duracao == 1 else f"{duracao} dias"
            data = '' if data == None else data
            duracao = '' if duracao == None else duracao
            self.tabela_pesquisa_m.insert('', END, values=(id_veiculo, id_manutencao, placa, detalhes, data, duracao))

    def data_atual_manutencao(self):
        #FUNÇÃO PARA INSERIR A DATA ATUAL NA ENTRY CASO O CHECKBOX ESTEJA MARCADO
        hoje = datetime.now()
        hoje = hoje.strftime("%d/%m/%Y")
        if self.check_valor3.get() == 1:
            self.ent_data_inicio.delete(0,11)
            self.ent_data_inicio.insert(0,hoje)
        if self.check_valor3.get() == 0:
            self.ent_data_inicio.delete(0,11)
            self.ent_data_inicio.insert(0,"DD/MM/AAAA")