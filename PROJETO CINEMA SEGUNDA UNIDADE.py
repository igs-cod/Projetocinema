import emojis


sala1 = []
sala2 = []
sala3 = []
adm = {} #dicionario pra armazenar os usuarios e o adm ( o adm será o primeiro que se cadastrar)
#o dicionario adm ta armazenando tanto o adm quanto os usuarios do sistema
#eu poderia mudar o nome do dicionario para adm_usari .



       # inicio do loop menu geral do cine sertao


                                     #033 é um codigo pra mudar a cor no terminal
while (True):
    op_mg = input( '|=============== \033[94mMENU GERAL \033[0m ================== \n'
                   '|\n'                                         
                   '| \033[93;1m   1- Gerenciar os filmes (ADM) \033[0m \n'         
                   '|  \033[93;1m  2- Comprar Ingressos (CLIENTE) \033[0m   \n'  
                   '|  \033[93;1m  3- Cadastrar usuário (ADM ou CLIENTE) \033[0m  \n'
                   '|  \n'
                   '| --------------------------------------------\n'                                            
                   '  \033[95m      Qual opçao voce vai escolher  : \033[0m\n '

    )



      # opçao 1 do menu geral
    if (op_mg == '1'):
        usuario = input(' digite seu usuario adm :\n')
        senha = input('digite sua senha adm : \n')

        logado = False

        for chave in adm:
            if (chave == usuario and adm[usuario][1] == senha):
                logado = True
            else:
                print(emojis.encode(' \033[31m voce nao pode usar essa opção  \u274C \033[0m \n'))
                break



           # se a variavel boleana for verdadeira apresente o menu do ADM


            if (logado):
                print (emojis.encode(' \033[92m ADM no comando \u2705 \033[0m \n'))
                op_m_adm = input( '|=============== \033[94m MENU ADM \033[0m ================== \n'
                   '|\n'                                         
                   '| \033[93;1m   1- Cadastrar filme \033[0m \n'         
                   '|  \033[93;1m  2- Buscar filme  \033[0m   \n'  
                   '|  \033[93;1m  3- Atualizar dados do filme \033[0m  \n'
                   '|  \033[93;1m  4- Remover filme \033[0m  \n'
                   '|  \033[93;1m  5 - listas filmes em salas \033[0m  \n'  
                   '|  \033[93;1m  6 - listas usuarios cadastrados \033[0m  \n' 
                   '|  \033[93;1m  0- Pra voltar ao Menu Geral \033[0m  \n'
                                  '\n'
                   '| --------------------------------------------\n'                                            
                   '  \033[95m      Qual opçao voce vai escolher  : \033[0m\n '

    )

                if (op_m_adm == '1'):

                    filme = input(' Qual o nome do   filme : ')

                    horari = int(input(' Qual será o horario desse filme : '))
                    capaci = int(input(' qual a capacidade da sala  : '))


                   #CRIANDO O DICIONARIO _NOVFILME
                   # CADA DICIONARIO É UM FILME
                   # A CHAVE DO DICIONARIO É O NOME DO FILME
                   # E OS VALORES É UMA LISTA COM O HORATIO E A CAPACIDADE

                    nov_filme = {filme:[horari,capaci]}


                    sala_a_ir = input('qual  sala vai ta esse filme ?')

                    #  de acordo com as condiçoes dependendo do q  o adm digitar
                    # o DICIONARIO  vai parar em uma das  3 listas

                    if (sala_a_ir == '1'):
                        sala1.append(nov_filme)

                    elif (sala_a_ir == '2'):
                        sala2.append(nov_filme)

                    else:
                        sala_a_ir == '3'
                        sala3.append(nov_filme)

                    print('====== Filmes da sala 1 ======  \n')
                    print(sala1)
                    print('====== Filmes da sala 2 ======  \n')
                    print(sala2)
                    print('====== Filmes da sala 3 ======  \n')
                    print(sala3)



                    perg = input(' Quer continuar cadastrando filme ? : \n'
                                 's- para cadastrar mais e n- para sair ')


                    while (perg == 's'):
                        filme = input(' Qual o nome do   filme : ')

                        horari = int(input(' Qual será o horario desse filme : '))
                        capaci = int(input(' qual a capacidade da sala  : '))

                        nov_filme = {filme: [horari, capaci]}

                        sala_a_ir = input('qual  sala vai ta esse filme ?')




                        if (sala_a_ir == '1'):
                            sala1.append(nov_filme)

                        elif (sala_a_ir == '2'):
                            sala2.append(nov_filme)

                        else:
                            sala_a_ir == '3'
                            sala3.append(nov_filme)

                        print('====== Filmes da sala 1 ======  \n')
                        print(sala1)
                        print('====== Filmes da sala 2 ======  \n')
                        print(sala2)
                        print('====== Filmes da sala 3 ======  \n')
                        print(sala3)


                        perg = input(' Quer continuar cadastrando filme ? : \n'
                                     's- para cadastrar mais e n- para sair ')



                        if (perg == 'n'):
                            print(' \033[95m ok saindo de cadastro \033[0m ')
                            break


                elif (op_m_adm == '2'):

                    procura = input('Qual filme você vai procurar: ')



                    for dic in sala1:
                        if procura in dic:

                            print(f'o filme {procura} está cadastrado na sala 1')
                            break

                    else:
                        print('nao temos esse filme na sala 1')


                    for dic in sala2:
                        if procura in dic:

                            print(f'o filme {procura} está cadastrado na sala 2')
                            break
                    else:
                        print('nao temos esse filme na sala 2')


                    for dic in sala3:
                        if procura in dic:

                            print(f'o filme {procura} está cadastrado na sala 3')
                            break
                    else:
                        print('nao temos esse filme na sala 3\n')



                elif (op_m_adm == '3'):
                      print('opçao incopleta')
                      break





                #opcao remover incopleta
                elif (op_m_adm == '4'):

                     apagar = input('Qual filme você quer remover ?')
                     if apagar in sala1 or apagar in sala2 or apagar in sala3:
                         nov_filme.pop(apagar)


                         print('====== Filmes da sala 1 ======  \n')
                         print(sala1)
                         print('====== Filmes da sala 2 ======  \n')
                         print(sala2)
                         print('====== Filmes da sala 3 ======  \n')
                         print(sala3)


                elif (op_m_adm == '5'):
                    print('====== Filmes da sala 1 ======  \n')
                    print(sala1)
                    print('====== Filmes da sala 2 ======  \n')
                    print(sala2)
                    print('====== Filmes da sala 3 ======  \n')
                    print(sala3)


                elif (op_m_adm == '6'):
                    print(adm)


                else:
                    (op_m_adm == '0')
                    print('voltando ao menu geral')
                    break


    if (op_mg == '2'):

    #ADM Ta acessando essa opçao . falta corrigir
        logado = True

        usuario = input('digite seu usuario adm :')
        senha = input('digite sua senha adm : ')

        if (usuario in adm):
            logado = True


            if (logado):

                print('====== Filmes da sala 1 ======  \n')
                print(sala1)
                print('====== Filmes da sala 2 ======  \n')
                print(sala2)
                print('====== Filmes da sala 3 ======  \n')
                print(sala3)

                compra = input('qual filme voce quer assistir  ?')

                # para cada dicionario na lista se compra for igual a variavel iter (que é a chave)
                # escreva a chave (nome do filme) e a sala
                for fil in sala1:
                    if (compra in fil):
                        print(f' voce escolheu  o filme {compra} na sala 1 ')
                    else:
                        print(' \033[31m  nao existe esse filme nessa sala \033[0m')

                for fil in sala2:
                    if (compra in fil):
                        print(f' voce escolheu  o filme {compra} na sala 2 ')
                    else:
                        print(' \033[31m nao existe esse filme nessa sala \033[0m')

                for fil in sala3:
                    if (compra in fil):
                        print(f' voce escolheu  o filme {compra} na sala 3 ')
                    else:
                        print(' \033[31m nao existe esse filme nessa sala \033[0m')


        #usuario = input('digite seu usuario : ')
        #if usuario in adm


            #while usuario not in adm:
                #usuario = input('digite o usuario cadastrado :')


    if (op_mg == '3'):
        nome = input('digite seu nome')
        if '@cine.com' in nome:
            print('nome invalido - digite sem arroba')

            # se o usuario digitar  @cine.com no valor da variavel nome
            # o programa nao vai aceitar e vai continuar pedindo um nome
            # ate que o nome nao tenha @cine.com

            while '@cine.com' in nome:
                nome = input('digite seu nome de forma correta')
        usu_adm = input('digite um nome de usuario com @cine.com :')
        if (usu_adm in adm) :
            print(' \033[31m usuario ja cadastrado cadastrado \033[0m ')
            while usu_adm in adm:
                usu_adm = input(' \033[95m digite um nome de usuario valido  : \033[0m')



        if ('@cine.com' not in usu_adm):
            print(emojis.encode(' \033[31m usuario invalido  \u274C \033[0m '))
            while '@cine.com' not in usu_adm:
              usu_adm = input(' \033[95m digite um nome de usuario : \033[0m')

        senha_adm = input(' crie uma senha de no mínimo 8 caracteres : ')
        while len(senha_adm) < 8  :
            print(emojis.encode(' \033[31m senha esta curta \u274C. Digite uma senha com 8 caracteres \033[0m '))
            senha_adm = input(' \033[95m  crie uma senha : \033[0m ')
        while nome in senha_adm:
            print(emojis.encode(' \033[31m a senha nao pode ter seu nome \u274C. Digite uma senha mais forte \033[0m '))
            senha_adm = input(' \033[95m  crie uma senha sem seu nome : \033[0m ')

        adm[usu_adm] = [nome,senha_adm]




        print(f'Nome: {adm[usu_adm][0]}')
        print(f'Usuário: {usu_adm}')
        print(f'Senha: {adm[usu_adm][1]}')

                                            # barra U seguido de numeros é um codigo pra colocar emoji.
                                            # que veio do pacote importado emojis
        print (emojis.encode(' \033[92m  Cadastrado com sucesso  \u2705 \033[0m \n'))

















