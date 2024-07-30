def calcular_area_do_quadrado(lado):
    return lado ** 2
resultado  = calcular_area_do_quadrado(15)
print(f'A area do quadrado é {resultado} m2')

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))

resultado = brincar_de_plim(100)

def print_hi(name):
    print(f'oi, {name}')

if __name__ == '__main__':
    print_hi ('Guilherme')
def dias_if(escolha):
    if escolha == 1:
        print('O dia da semana é segunda')
    elif escolha == 2:
        print('O dia da semana é terça')
    elif escolha == 3:
        print('O dia da semana é quarta')
    else:
        print('outro dia')

dias_if(4)


def dias_da_semana_case(dia):
    match dia:
        case 1:
            print('O dia é segunda')
        case 2:
            print('o dia é terça')
        case _:
            print('outro dia')

dias_da_semana_case(1)
def bricar_de_para_ou_continua():
    resposta = 'C'    #continua

while resposta == 'C' or resposta == 'c':
    resposta = input("Digete P para parar ou C para continuar")

print('voce decidiu parar com a brincadeira')

calcular_area_do_quadrado()

bricar_de_para_ou_continua()