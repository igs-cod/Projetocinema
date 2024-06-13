
from funcoes.funcoes_usu import menu_cliente
from funcoes.funcoes_adm import menu_adm

from dados import list_filmes, clientes, adms,ingre_compra


def login_geren_fil():

    login = input(' digite seu usuario  :\n')
    senha = input(' digite sua senha  :\n')

    logado = False

    for admin in adms:
        # se vai entrar se o email e senha tiver correto
        # se um dos 2 nao tiver correto ele nao entra
        if (login == admin['usuario'] and senha == admin['senha']):
            logado = True
            print('adm no comando')
            break
        # break pra parar o loop pq ja encotrou o adm

    else:
        print('opçao disponivel apenas para adms com cadastro')
    # print('nao existe esse adm\nessa opçao nao é disponivel pra cliente')

    if (logado == True):
        menu_adm()


def login_comp_ingr():
    log_cl = input(' digite seu usuario  :\n')
    sen_cl = input(' digite sua senha  :\n')

    logado = False

    for dic_client in clientes:
        # se vai entrar se o email e senha tiver correto
        # se um dos 2 nao tiver correto ele nao entra
        if (log_cl == dic_client['usuario'] and sen_cl == dic_client['senha']):
            logado = True
            print('voce pode comprar engresso')
            break
        # break pra parar o loop pq ja encotrou o cliente
    else:
        logado = False
        print('apenas clientes com cadastro pode comprar ingressos')

    if (logado == True):
        menu_cliente()


def login_cadas_us():
    op_us = input(' 1 - para ADM 2- para Cliente \n Quem voce quer ser ? ')

    if (op_us == '1'):

        nome_adm = input(' digite seu nome')
        if ('@' in nome_adm):
            print('nome invalido')
            while ('@' in nome_adm):
                nome_adm = input(' nome invalido digite seu nome de forma correta')

        us_adm = input(' digite seu email')
        if ('@' not in  us_adm):
            print('email invalido')
            while ('@' not in us_adm):
                us_adm = input(' digite um email com @')

        for usuarios_adms in adms:
            if (usuarios_adms ['usuario'] == us_adm):
               print('usuario ja cadastrado')
               while (us_adm in usuarios_adms ['usuario']):
                   us_adm = input(' digite outro email')

        if (nome_adm == us_adm):
            print('seu usuario nao pode ser seu nome')
            while (nome_adm == us_adm):
                us_adm = input(' digite um email valido')

        senha_adm = input(' digite sua senha de no minino 8 caracteres')
        while (len(senha_adm) < 8):
            print(' \033[31m senha esta curta \u274C. Digite uma senha com 8 caracteres \033[0m ')
            senha_adm = input(' digite sua senha de no minino 8 caracteres')

        adm = {'nome': nome_adm, 'usuario': us_adm, 'senha': senha_adm}
        adms.append(adm)
        print("\n" + "-" * 30 + "\n")
        print('ADM cadastrado com sucesso ')
        print('Seus dados : ')
        print('\n')
        print(f'Nome : {nome_adm}')
        print(f'Usuário: {us_adm}')
        print(f'Senha: {senha_adm}')
        print("\n" + "-" * 30 + "\n")



    elif (op_us == '2'):

        nome_cli = input(' digite seu nome')
        if ('@' in nome_cli):
            print('nome invalido')
            while ('@' in nome_cli):
                nome_cli = input('  digite seu nome de forma correta')

        us_cli = input('Digite seu email: ')
        if ('@' not in  us_cli):
            print('email invalido tem quer @')
            while ('@' not in us_cli):
                us_cli = input(' digite um email com @')

        for usuarios_clie in clientes:
            if (usuarios_clie['usuario'] == us_cli):
                print('usuario cliente  ja cadastrado')
                while  (us_cli in usuarios_clie['usuario']):
                    us_cli = input('Digite outro email: ')

        for emai_cli in clientes:
            if (emai_cli['usuario'] == us_cli):
                print('email ja existente digite outro')
                while (emai_cli['usuario'] == us_cli):
                    us_cli = input('Digite outro email: ')

        for usuarios_adms in adms:
            if (usuarios_adms ['usuario'] == us_cli):
                print('usuario   cadastrado como adm')
                while  (us_cli in usuarios_adms['usuario']):
                    us_cli = input('Digite outro email: ')



        if ('@' not in us_cli):
            print('seu usuario tem que ter @')
            while ('@' not in us_cli):
                us_cli = input(' digite um email com @')
        senha_cli = input(' digite uma senha de 8 caracteres')
        while (len(senha_cli) < 8):
            print(' \033[31m senha esta curta \u274C. Digite uma senha com 8 caracteres \033[0m ')
            senha_cli = input(' digite sua senha de no minino 8 caracteres')

        cliente = {'nome': nome_cli, 'usuario': us_cli, 'senha': senha_cli}
        clientes.append(cliente)
        print("" + "-" * 30 + "")
        print('Cliente cadastrado com sucesso ')
        print('Seus dados : ')

        print(f'Nome : {nome_cli}')
        print(f'Usuário: {us_cli}')
        print(f'Senha: {senha_cli}')
        print("" + "-" * 30 + "")

    else:
        print('opção inválida')





def listar_filmes():
    for cada_filme in list_filmes:
        print(f'Título: {cada_filme['titulo']}')
        print(f'Sala: {cada_filme['sala']}')
        print(f'Horario: {cada_filme['horario']} horas')
        print(f'Capacidade: {cada_filme['capacidade']} pessoas')
        print(f'Preço do  Ingresso: {cada_filme['preço']} R$')
        print(f'Sinopse: {cada_filme['sinopse']}')
        print(f'Gênero: {cada_filme['genero']}')
        print("\n" + "-" * 30 + "\n")
    if len(list_filmes) == 0:
        print(f'A quantidade de  filmes  cadastrado é {len(list_filmes)} ')
    else:
        print(f'A quantidade de  filmes  cadastrado é {len(list_filmes)} ')



#essa def aqui nao precisa mais nao
def menu_geral ():
    while True:
        escolha = input('|=============== \033[94mMENU GERAL \033[0m ==================\n'
                        '| \033[93;1m   0- Para encerrar o programa \033[0m  \n'
                        '| \033[93;1m   1- Gerenciar os filmes (ADM) \033[0m \n'
                        '|  \033[93;1m  2- Comprar Ingressos (CLIENTE) \033[0m   \n'
                        '|  \033[93;1m  3- Cadastrar usuário (ADM ou CLIENTE) \033[0m  \n'
                        '|  \033[93;1m  4- Listar filmes \033[0m  \n'
                        '| --------------------------------------------\n'
                        '  \033[95m      Qual opção você vai escolher  : \033[0m\n'
                        )

        if escolha == '0':
            break
        elif escolha == '1':
            login_geren_fil()
        elif escolha == '2':
            login_comp_ingr()
        elif escolha == '3':
            login_cadas_us()
        elif escolha == '4':
            listar_filmes()
        else:
            print('opção inválida')
























