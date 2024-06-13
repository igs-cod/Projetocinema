import emojis
from dados import list_filmes, clientes, adms, ingre_compra



def comprar_ingressos():
    for cada_filme in list_filmes:
        print(f'Título: {cada_filme['titulo']}')
        print(f'Sala: {cada_filme['sala']}')
        print(f'Horario: {cada_filme['horario']} horas')
        print(f'Capacidade: {cada_filme['capacidade']} pessoas')
        print(f'Preço do  Ingresso: {cada_filme['preço']} R$')
        print(f'Sinopse: {cada_filme['sinopse']}')
        print(f'Gênero: {cada_filme['genero']}')
        print("\n" + "-" * 30 + "\n")

    ingres = input('voce quer comprar ingressos pra qual filme?')
    filme_encon = False
    for fil in list_filmes:
        if (fil['titulo'] == ingres):
            filme_encon = True

            print(f' Dados do filme :  ')
            print(f' Titulo do filme  :  {fil['titulo']} ')
            print(f' Sala que o filme está :  Nome : {fil['sala']} ')
            print(f' Horario do filme  : {fil['horario']} ')
            print(f' Capacidade do filme :  {fil['capacidade']} ')
            print(f' Valor do Ingresso :  {fil['preço']} ')
            print(f' Gênero do filme   : {fil['genero']} ')
            print(f' Sinopse do filme  :  {fil['sinopse']}')
            print(f'\n')

            nome_usu = input('digite seu nome')

            rg = input('digite seu RG ')
            while len(rg) < 5:
                print('RG tem que ser maior que 5 números')
                rg = input('digite seu rg correto ')
            for regis in ingre_compra:
                if regis['identidade'] == rg:
                    print('rg ja cadastrado')
                    while rg  not in regis['identidade']:
                        rg = input(' digite seu RG, ele é unico')


            qt_ing = int(input('voce quer comprar  quantos ingressos?'))
            for regis in ingre_compra:
                if regis['quantidade'] > 10:
                    print('voce nao pode comprar mais ingressos')
                    break

            if (qt_ing < 0):
                print('filme esgotado escolha outro')
            while (qt_ing > 10):
                print('voce so pode comprar até 10 ingressos')
                qt_ing = int(input('voce quer comprar  quantos ingressos? só vale até 10'))
            print(f'voce comprou {qt_ing} para o filme{ingres} bom filme pra você')


            # dicionario registro pra guardar informaçoes dos ingresso comprado pelo cliente
            regis_ing_cli = {'identidade': rg, 'nome': nome_usu, 'ingresso': ingres, 'quantidade': qt_ing}
            ingre_compra.append(regis_ing_cli)

            fil['capacidade'] -= qt_ing


    if (not filme_encon):
        print('nao temos esse filme no cinema')





def listar_tds_ing_cli():
    proc_in_cl = input('digite seu rg para ver a lista de ingresso comprado ?')

    # registro é um dicionario que ta armazenado o nome, o ingresso do filme que ele
    # comprou e a quantidade de ingresso
    for reg_cl in ingre_compra:
        if (reg_cl['identidade'] == proc_in_cl):
            print(f'Nome: {reg_cl['nome']}, Filme: {reg_cl['ingresso']}, Quantidade: {reg_cl['quantidade']}')




        else:
            print('essa pessoa nao comprou ingresso')




def busc_fil_p_gen():
    busc_gen = input('qual gênero de filmes vc quer pesquisar')

    for fil_gen in list_filmes:
        if (fil_gen['genero'] == busc_gen):
            filme_encon = True

            print(f' Dados do filme :  ')
            print(f' Titulo do filme  :  {fil_gen['titulo']} ')
            print(f' Sala que o filme está : {fil_gen['sala']} ')
            print(f' Horario do filme  : {fil_gen['horario']} ')
            print(f' Capacidade do filme :  {fil_gen['capacidade']} ')
            print(f' Valor do Ingresso :  {fil_gen['preço']} ')
            print(f' Gênero do filme   : {fil_gen['genero']} ')
            print(f' Sinopse do filme  :  {fil_gen['sinopse']}')
            print(f'\n')







def menu_cliente():
    while (True):
        print(' \033[92m Bem vindo ao nosso cinema \u2705 \033[0m \n')
        opcao_cli = input('|=============== \033[94m MENU CLIENTE \033[0m ================== \n'
                         '|  \033[93;1m  0- Pra voltar ao Menu Geral \033[0m  \n'
                         '| \033[93;1m   1- Comprar ingressos \033[0m \n'
                         '|  \033[93;1m  2-Listar todos os ingressos comprados pelo cliente \033[0m  \n'
                         '|  \033[93;1m  3-buscar filme por genero  \033[0m  \n'

                         '| --------------------------------------------\n'
                         '  \033[95m      Qual opçao voce vai escolher  : \033[0m\n '

                         )

        if (opcao_cli == '0'):
            break
        elif (opcao_cli == '1'):
            comprar_ingressos()
        elif (opcao_cli == '2'):
            listar_tds_ing_cli()
        elif (opcao_cli == '3'):
            busc_fil_p_gen()
        else:
            print('opção inválida \n Digite um número  entre 0 a 3')












