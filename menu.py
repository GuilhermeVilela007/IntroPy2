def calcular_area_do_quadrado(lado):
    return lado ** 2

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))

def sair():
    print('Obrigado e Volte Sempre')
    return False

def exibir_menu(escolha):
    opcao = {
        1: calcular_area_do_quadrado(2),
        2: brincar_de_plim(60),
        3: print_hi('Guilherme'),
        4: sair(),
    }
    return opcao.get(escolha, 'Opção Invalida')

def print_hi(name):
    print(f'oi, {name}')

if __name__ == '__main__':
    continua = True

    #while continua:
    print('#################################################')
    print('#                                               #')
    print('#           M E N U  D E  O P Ç O E S           #')
    print('#          1 - Brincar de PLIM                  #')
    print('#          2 - Area do Quadrado                 #')
    print('#          3 - Nome                             #')
    print('#                                               #')
    print('#          Z - Sair                             #')
    print('#################################################')

    escolha = input("Escolha sua opção")
    #print(f'A sua escolha foi: {escolha}')
    exibir_menu(escolha)



