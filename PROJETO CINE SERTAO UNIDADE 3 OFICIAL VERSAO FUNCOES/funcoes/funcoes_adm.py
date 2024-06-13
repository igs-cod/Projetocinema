import emojis
from dados import list_filmes, clientes, adms, ingre_compra


def cadastrar_filme():
    nom_filme = input(' Qual o nome do filme : ')
    sala_fil = int(input('Qual a sala do filme ?'))
    horari = input('Qual o horario do filme ?')
    capaci = int(input('Qual a capacidade da sala'))
    valor_ing = float(input('Qual o valor do ingresso ?'))
    gener = input('Qual o Gênero do filme ?')
    sinop = input('Digite um breve resumo do filme')

    filme = {'titulo': nom_filme, 'sala': sala_fil, 'horario': horari, 'capacidade': capaci,
             'preço': valor_ing, 'genero': gener, 'sinopse': sinop}
    list_filmes.append(filme)

    print("\n" + "-" * 30 + "\n")
    print(f'Filme {nom_filme} cadastrado com sucesso')
    print(f'Título do filme : {nom_filme}')
    print(f'Sala que o filme está: Sala {sala_fil}')
    print(f'Horario de exibição: {horari} horas')
    print(f'Capacidade da sala : {capaci} pessoas')
    print(f'Valor do engresso: {valor_ing} R$')
    print(f'Gênero do filme: {gener}')
    print(f'Sinopse do filme: {sinop}')
    print("\n" + "-" * 30 + "\n")
    cont_add = input(' Quer continuar cadastrando filme ? : \n'
                     'S- para cadastrar mais e N- para sair ').lower()

    while (cont_add == 's'):
        nom_filme = input(' Qual o nome do   filme : ')
        sala_fil = int(input('Qual a sala do filme ?'))
        horari = input('Qual o horario do filme ?')
        capaci = int(input('Qual a capacidade da sala'))
        valor_ing = float(input('Qual o valor do ingresso ?'))
        gener = input('Qual o Gênero do filme ?')
        sinop = input('Digite um breve resumo do filme')

        filme = {'titulo': nom_filme, 'sala': sala_fil, 'horario': horari, 'capacidade': capaci,
                 'preço': valor_ing, 'genero': gener, 'sinopse': sinop}

        list_filmes.append(filme)

        print("\n" + "-" * 30 + "\n")
        print(f'Filme{nom_filme}cadastrado com sucesso')
        print(f'Título do filme : {nom_filme}')
        print(f'Sala que o filme está: {sala_fil}')
        print(f'Horario de exibição: {horari}')
        print(f'Capacidade da sala : {capaci}')
        print(f'Valor do engresso: {valor_ing}')
        print(f'Gênero do filme: {gener}')
        print(f'Sinopse do filme: {sinop}')
        print("\n" + "-" * 30 + "\n")

        cont_add = input(' Quer continuar cadastrando filme ? : \n'
                         'S- para cadastrar mais e N- para sair ').lower()

        if (cont_add == 'n'):
            print(' \033[95m ok saindo de cadastro de filme \033[0m ')
            break




def buscar_filme():
    busc_fil = input('digite o nome do filme que voce quer achar')
    achar_film = False

    for dic_filme in list_filmes:
        if (dic_filme['titulo'] == busc_fil):
            achar_film = True
            print(f' filme encontrado : \n  ')
            print(f' Titulo do filme  :  {dic_filme['titulo']}\n ')
            print(f' Sala que o filme está :  {dic_filme['sala']}\n ')
            print(f' Horario do filme  : {dic_filme['horario']}\n ')
            print(f' Capacidade do filme :  {dic_filme['capacidade']}\n ')
            print(f' Valor do Ingresso :  {dic_filme['preço']}\n ')
            print(f' Gênero do filme   : {dic_filme['genero']}\n ')
            print(f' Sinopse do filme  :  {dic_filme['sinopse']}\n ')

    if (not achar_film):
            print('O Filme que voce está buscando não está cadastrado no cinema')



def atualizar_fil():
    atua_filme = input('digite o nome do filme que voce quer atualizar ?')

    for indice in range(len(list_filmes)):
        if (list_filmes[indice]['titulo'] == atua_filme):


            # esta linha verifica se o título do filme no índice atual da
            # list_filmes é igual ao nome do filme que o usuário digitou

            nom_filme = input(' Qual o nome do   filme : ')
            list_filmes[indice]['titulo'] = nom_filme

            sala_fil = int(input('Qual a sala do filme ?'))
            list_filmes[indice]['sala'] = sala_fil

            horari = input('Qual o horario do filme ?')
            list_filmes[indice]['horario'] = horari

            capaci = int(input('Qual a capacidade da sala'))
            list_filmes[indice]['capacidade'] = capaci

            valor_ing = float(input('Qual o valor do ingresso ?'))
            list_filmes[indice]['preço'] = valor_ing

            gener = input('Qual o Gênero do filme ?')
            list_filmes[indice]['genero'] = gener

            sinop = input('Digite um breve resumo do filme')
            list_filmes[indice]['sinopse'] = sinop
            break
    else:
        print('nao temos esse filme cadastrado')





def remover_filme():
    for cada_filme in list_filmes:
        print(f'Título: {cada_filme['titulo']}')
        print(f'Sala: {cada_filme['sala']}')
        print(f'Horario: {cada_filme['horario']} horas')
        print(f'Capacidade: {cada_filme['capacidade']} pessoas')
        print(f'Preço do  Ingresso: {cada_filme['preço']} R$')
        print(f'Sinopse: {cada_filme['sinopse']}')
        print(f'Gênero: {cada_filme['genero']}')
        print("\n" + "-" * 30 + "\n")
    remov_fil = input('qual filme voce deseja remover : ')

    for indice_dic in range(len(list_filmes)):
        if (list_filmes[indice_dic]['titulo'] == remov_fil):
            del list_filmes[indice_dic]
            print('filme removido')
            for cada_filme in list_filmes:
                print(f'Título: {cada_filme['titulo']}')
                print(f'Sala: {cada_filme['sala']}')
                print(f'Horario: {cada_filme['horario']} horas')
                print(f'Capacidade: {cada_filme['capacidade']} pessoas')
                print(f'Preço do  Ingresso: {cada_filme['preço']} R$')
                print(f'Sinopse: {cada_filme['sinopse']}')
                print(f'Gênero: {cada_filme['genero']}')
                print("\n" + "-" * 30 + "\n")


    else:
        print('filme nao encontrado')





def listar_tds_ing_v():
    for regis_cl in ingre_compra:
        tot_in_comp = 0
        print(f'nome : {regis_cl['nome']},filme {regis_cl['ingresso']},{regis_cl['quantidade']}')
        tot_in_comp = tot_in_comp + regis_cl['quantidade']

    print(f'total de ingressos comprados foi{tot_in_comp}')



def lis_td_ing_v_f():

    bus_ing_v_f = input('qual filme voce quer ver os ingressos vendidos ?')

    for regis_cl in ingre_compra:
        if (regis_cl ['ingresso'] == bus_ing_v_f):
            print(f' total de {regis_cl['ingresso'] } ingressos vendidos')



def gerar_ar_filmes():
    with open('listafilmes.txt', 'a') as arquivo_filmes:
        for cada_filme in list_filmes:
            arquivo_filmes.write(f'Título: {cada_filme['titulo']}\n')
            arquivo_filmes.write(f'Sala: {cada_filme['sala']}\n')
            arquivo_filmes.write(f'Horario: {cada_filme['horario']} horas\n')
            arquivo_filmes.write(f'Capacidade: {cada_filme['capacidade']} pessoas\n')
            arquivo_filmes.write(f'Preço do Ingresso: {cada_filme['preço']} R$\n')
            arquivo_filmes.write(f'Gênero: {cada_filme['genero']}\n')
            arquivo_filmes.write(f'Sinopse: {cada_filme['sinopse']}\n')
            arquivo_filmes.write("\n" + "-" * 30 + "\n")










def menu_adm():
    while (True):
        print(' \033[92m ADM no comando \u2705 \033[0m \n')
        opcao_adm = input('|=============== \033[94m MENU ADM \033[0m ================== \n'
                         '| \033[93;1m   1- Cadastrar filme \033[0m \n'
                         '|  \033[93;1m  2- Buscar filme  \033[0m   \n'
                         '|  \033[93;1m  3- Atualizar dados do filme \033[0m  \n'
                         '|  \033[93;1m  4- Remover filme \033[0m  \n'
                         '|  \033[93;1m  5 - Listar todos os  ingressos vendidos) \033[0m  \n'
                         '|  \033[93;1m  6 - Listar todos os  ingressos vendidos de um filme específico \033[0m  \n'
                         '|  \033[93;1m  7 - Gerar arquivo de todos os filmes \033[0m  \n'
                         '|  \033[93;1m  0- Pra voltar ao Menu Geral \033[0m  \n'
                         '| --------------------------------------------\n'
                         '  \033[95m      Qual opçao voce vai escolher  : \033[0m\n '

                         )



        if (opcao_adm == '0'):
            break
        elif (opcao_adm =='1'):
            cadastrar_filme()
        elif (opcao_adm == '2'):
            buscar_filme()
        elif (opcao_adm == '3'):
            atualizar_fil()
        elif (opcao_adm == '4'):
            remover_filme()
        elif (opcao_adm == '5'):
            listar_tds_ing_v()
        elif (opcao_adm == '6'):
            lis_td_ing_v_f()
        elif (opcao_adm == '7'):
            gerar_ar_filmes()

        else:
            print('opcao invalida')













