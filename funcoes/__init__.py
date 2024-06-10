def somar ():
    num1 = float(input('digite um numero : '))
    num2 = float(input('digite outro numero : '))
    resultado = num1 + num2
    print(resultado)


def subtrair ():
    num1 = float(input('digite um numero : '))
    num2 = float(input('digite outro numero : '))
    resultado = num1 - num2
    print(resultado)

def multiplicar ():
    num1 = float(input('digite um numero : '))
    num2 = float(input('digite outro numero : '))
    resultado = num1 * num2
    print(resultado)

def dividir ():
    num1 = float(input('digite um numero : '))
    num2 = float(input('digite outro numero : '))
    resultado = num1 / num2
    print(resultado)


opcao = 1

while opcao :
    print('0 - sair')
    print('1- somar')
    print('2- subtrair')
    print('3- multiplicar')
    print('4- dividir')

    opcao = int(input('escolha a opcçao:'))

    if(opcao == 1 ):
        somar()
    elif (opcao == 2):
        subtrair()
    elif (opcao == 3):
        multiplicar()
    elif (opcao == 4):
        dividir()






