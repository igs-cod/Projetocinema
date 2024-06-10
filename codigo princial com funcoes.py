from funcoes_menugeral import login_geren_fil,login_comp_ingr,login_cadas_us,listar_filmes


#import emojis
from dados import list_filmes, clientes, adms, ingre_compra




while(True):
        escolha = input('|=============== \033[94mMENU GERAL \033[0m ================== \n'
                      '| \033[93;1m   0- Para encerrar o programa \033[0m  \n'
                      '| \033[93;1m   1- Gerenciar os filmes (ADM) \033[0m \n'
                      '|  \033[93;1m  2- Comprar Ingressos (CLIENTE) \033[0m   \n'
                      '|  \033[93;1m  3- Cadastrar usuário (ADM ou CLIENTE) \033[0m  \n'
                      '|  \033[93;1m  4- listar filmes   \033[0m  \n'
                      '| --------------------------------------------\n'
                      '  \033[95m      Qual opçao voce vai escolher  : \033[0m\n '

                      )


        if escolha == '0':
             break
        elif escolha =='1':
            login_geren_fil()
        elif escolha == '2':
            login_comp_ingr()
        elif escolha == '3':
            login_cadas_us()
        elif escolha == '4':
            listar_filmes()
        else:
             print('opcao invalida')

# ta dando bug em atualizar filme
