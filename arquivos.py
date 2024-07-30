# 1 - importação de pacotes
import json
import pytest

#2 - Classe


#3 - definiçÕes(funçoes e Metodos)

dados = {}

dados['clientes'] = [] #indica a criação de um vetor, uma lista
dados['clientes'].append({
    'nome':'Guilherme',
    'telefone':'27999999999',
    'email':'teste@gmail.com'
})
dados['clientes'].append({
    'nome':'Marcielli',
    'telefone':'27888888888',
    'email':'marcielli@gmail.com'
})
def criar_json():
    with open('clientes.json','w') as outfile:
        json.dump(dados,outfile,indent=2)

def ler_json():
    with (open('clientes.json') as outfile):
        dados = json.load(outfile)
        temp = ''
        #exibir no console
        for registro in dados['clientes']:
            print('nome: ' + registro['nome'])
            print('telefone: ' + registro['telefone'])
            print('email: ' + registro['email'])
            print('')


def testar_criar_json():
    criar_json()
    print(dados['clientes'])

def testar_ler_json():
    print('Leitura do JSON pr linha/campo')
    ler_json()


