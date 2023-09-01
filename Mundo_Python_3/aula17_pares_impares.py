pares = []
impares = []
lista = []
cont = 7

num = [[], []]
valor = 0

for c in range(0,7):
    valor = int(input(f'Digite um {c+1}º valor: '))
    if valor%2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
        
num[0].sort()
num[1].sort()
print(f'Os valores pares {num[0]}, os impares {num[1]}')


# while cont !=0:
#     lista.append(int(input('Digite um número: ')))
#     cont -= 1
#     for num in lista:
#         if num%2 == 0:
#             pares.append(lista[:])
#             lista.clear()
#         else:
#             impares.append(lista[:])
#             lista.clear()

# lista2 = []
# lista2.append(sorted(pares[:]))    
# lista2.append(sorted(impares[:]))


# print(f'A lista digitada foi {lista2}')
# print(f'Os números pares foram {pares} e impares {impares}')