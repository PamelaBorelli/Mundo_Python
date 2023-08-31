'''
Digite uma lisa que sorteia um item dela
'''

import random
# lista = []
# cont = 0
# nome = str(input('Digite o {}º nome: '.format(cont+1)))


# for cont in (lista, 3):
#     lista.append(nome)


# print("A lista digitada é: ",lista)

lista = ['Pamela', 'Joao', 'Jose', 'Paulo']
escolhido = random.choice(lista)
aleatorio = random.shuffle(lista)
print(aleatorio)
print("O nome escolhido foi: {}".format(escolhido))
print("A ordem de apresentação é {}".format(sorted(lista)))
