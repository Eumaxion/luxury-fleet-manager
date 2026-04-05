from app.modules import *

def legalizar_page(self):
    #ABA PARA MOSTRAR OS VEICULOS EM ALERTA DE LEGALIZAR
    legalizar = Frame(self.frame2)
    frame_legalizar = LabelFrame(legalizar, text="LEGALIZAR", font="sylfaen 16 bold")

    #TABELA COM OS VEICULOS QUE ESTÃO PRÓXIMOS A DATA DE LEGALIZAÇÃO
    self.tv_legalizar = ttk.Treeview(frame_legalizar, columns=('id', 'placa', 'data_de_aquisicao',
            'ultima_legalizacao', 'proxima_legalizacao', 'dias_proxima_legalizacao'), height=17, show='headings')
    self.tv_legalizar.column('id', minwidth=0, width=50)
    self.tv_legalizar.column('placa', minwidth=0, width=70)
    self.tv_legalizar.column('data_de_aquisicao', minwidth=0, width=150)
    self.tv_legalizar.column('ultima_legalizacao', minwidth=0, width=150)
    self.tv_legalizar.column('proxima_legalizacao', minwidth=0, width=150)
    self.tv_legalizar.column('dias_proxima_legalizacao', minwidth=0, width=100)
    self.tv_legalizar.heading('id', text='ID')
    self.tv_legalizar.heading('placa', text='PLACA')
    self.tv_legalizar.heading('data_de_aquisicao', text='DATA DE AQUISIÇÃO')
    self.tv_legalizar.heading('ultima_legalizacao', text='ULTIMA LEGALIZAÇÃO')
    self.tv_legalizar.heading('proxima_legalizacao', text='PRÓXIMA LEGALIZAÇÃO')
    self.tv_legalizar.heading('dias_proxima_legalizacao', text='DIAS RESTANTES')

    #FRAME COM OS WIDGETS PARA ATUALIZAR O STATUS DA LEGALIZAÇÃO
    frame_atualizar_status = LabelFrame(legalizar, text="Atualizar status", font="sylfaen 12 bold")
    self.label_id_legalizar = Label(frame_atualizar_status, text="ID do veiculo:", font="sylfaen 12")
    self.entry_id_legalizar = Entry(frame_atualizar_status)
    self.label_data_legalizar = Label(frame_atualizar_status, text="Data da legalização:", font="sylfaen 12")
    self.entry_data_legalizar = Entry(frame_atualizar_status)
    self.entry_data_legalizar.insert(0,"DD/MM/AAAA")
    self.check_valor2 = IntVar()
    self.check_data_atual = Checkbutton(frame_atualizar_status, text="Data atual", variable=self.check_valor2,
                                        offvalue=0, onvalue=1, command=lambda: self.data_atual_legalizar(self.check_valor2.get()))
    self.mensagem_legalizacao = Label(frame_atualizar_status, text="", font="sylfaen 12 bold", fg='red' )
    self.button_confirm_legalizar = Button(frame_atualizar_status, bd=5, cursor='hand2', relief="raised", bg='#743913',
                                            text="Confirmar", font="sylfaen 12 bold", command=lambda:self.atualizar_legalizacao(self.entry_data_legalizar.get(), self.entry_id_legalizar.get()))

    #POSICIONANDO A TABELA E OS WIDGETS NA FRAME
    self.tv_legalizar.grid(row=2, column=1, padx=8)
    self.tabela_legalizar()
    frame_atualizar_status.grid(row=3)
    self.label_id_legalizar.grid(row=1, column=0)
    self.entry_id_legalizar.grid(row=1, column=1)
    self.label_data_legalizar.grid(row=2, column=0)
    self.entry_data_legalizar.grid(row=2, column=1)
    self.check_data_atual.grid(row=2, column=2)
    self.mensagem_legalizacao.grid(row=3, column=0, columnspan=2)
    self.button_confirm_legalizar.grid(row=4, column=0, columnspan=2)
    frame_legalizar.grid(row=1)
    legalizar.pack(expand=TRUE, fill=BOTH)


def data_atual_legalizar(self,valor):
    #FUNÇÃO PARA INSERIR AUTOMATICAMENTE A DATA ATUAL CASO A CHECKBOX ESTEJA MARCADA
    hoje = datetime.today()
    hoje = hoje.strftime("%d/%m/%Y")
    if valor == 1:
        self.entry_data_legalizar.delete(0,11)
        self.entry_data_legalizar.insert(0,hoje)
    if valor == 0:
        self.entry_data_legalizar.delete(0,11)
        self.entry_data_legalizar.insert(0,"DD/MM/AAAA")

def tabela_legalizar(self):
    #QUERY PARA POPULAR A TABELA DE VEICULOS EM ALERTA PRÓXIMO A DATA DE LEGALIZAÇÃO
    self.tv_legalizar.delete(*self.tv_legalizar.get_children()) #excluindo tabelas ja existente
    data_atual = datetime.today()
    informacoes = [] #lista que vai receber as informações da tabela
    query_datas = ('SELECT id_veiculo, placa, data_de_aquisicao, ultima_legalizacao, proxima_legalizacao '
                    ' FROM automoveis ')
    datas_proxima_legalizacao = self.db_consulta(query_datas)
    for data in datas_proxima_legalizacao:
        #calculando quais itens estão com 10 dias de prioximidade da data de legalização
        data_proxima = datetime.strptime(data[4], "%d/%m/%Y")
        dias = data_proxima - data_atual
        if dias.days <= 10:
            data = list(data)
            data.append(dias.days + 1)
            informacoes.append(data)
    for item in informacoes:
        id, placa, data_de_aquisicao, ultima_legalizacao, proxima_legalizacao, dias_proxima_legalizacao = item
        nome_dias_proxima_legalizacao = "< 24 horas" if dias_proxima_legalizacao == 0 else (f"atrasado "
                f"{- dias_proxima_legalizacao} dia") if dias_proxima_legalizacao == -1 else (f"atrasado "
                f"{- dias_proxima_legalizacao} dias") if dias_proxima_legalizacao < -1 else (f"{dias_proxima_legalizacao}"
                f" dia") if dias_proxima_legalizacao == 1 else f"{dias_proxima_legalizacao} dias"
        nome_ultima_legalizacao = "Primeira legalização" if ultima_legalizacao == None else ultima_legalizacao
        self.tv_legalizar.insert('', 'end', values=(id, placa, data_de_aquisicao, nome_ultima_legalizacao,
                                                    proxima_legalizacao, nome_dias_proxima_legalizacao))

def testar_id(self, id):
    #TESTAR SE O ID INFORMADO EXISTE NA BASE DE DADOS
    query_placa = "SELECT id_veiculo FROM automoveis WHERE id_veiculo = ?"
    parametro_placa = [id]
    retorno = self.db_consulta(query_placa, parametro_placa)
    if len(retorno) != 0:
        return True
    else:
        return False

def atualizar_legalizacao(self, ultima, id_veiculo):
    #TESTES PARA VERIFICAR SE OS DADOS INFORMADOS ESTÃO CORRETOS PARA FAZER A ATUALIZAÇÃO DO STATUS DA LEGALIZAÇÃO DO VEICULO
    self.mensagem_legalizacao['text'] = ""
    id_vazia = True if id_veiculo == '' else False #testando se o campo id está preenchido
    data_vazia = True if ultima == '' else False #testando se o campo data está preenchido
    padrao_data = r'\d{2}/\d{2}/\d{4}'
    padrao_data_legal = re.match(padrao_data, ultima) #testando se a data está no formato indicado
    if id_vazia:
        self.mensagem_legalizacao['text'] = "Campo 'ID' obrigatório!"
        return
    if data_vazia:
        self.mensagem_legalizacao['text'] = "Campo 'DATA' obrigatório!"
        return
    if not padrao_data_legal:
        self.mensagem_legalizacao['text'] = "Data informada inválida!"
        return
    if self.testar_id(id_veiculo) == False: #testando se o veiculo existe na base de dados
        self.mensagem_legalizacao['text'] = "Veiculo não encontrado!"
        return
    proxima = datetime.strptime(ultima, "%d/%m/%Y") + timedelta(days=1826)
    # se tudo estiver corredo a proxima legalização deve ser a partir de 5 anos

    proxima = proxima.strftime("%d/%m/%Y")
    query_update_legalizacao = ("UPDATE automoveis SET ultima_legalizacao = ?,"
                                " proxima_legalizacao = ? WHERE id_veiculo = ?")
    parametros_update_legalizacao = ultima, proxima, id_veiculo
    self.db_consulta(query_update_legalizacao, parametros_update_legalizacao)
    self.mensagem_legalizacao['text'] = "Status atualizado com sucesso!"
    self.tabela_legalizar()