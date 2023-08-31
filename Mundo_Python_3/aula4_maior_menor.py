from random import randint
num = (5)
lista_numeros = []

for n in range(num):
    numero_aleatorio = randint(0,10)
    lista_numeros.append(numero_aleatorio)
    print(numero_aleatorio, end = ' ')
print(f'\nO maior número é: {max(lista_numeros)}')
print(f'O menor número é: {min(lista_numeros)}')






