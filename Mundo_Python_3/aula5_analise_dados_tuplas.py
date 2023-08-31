num = ()

par = 0

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite mais um outro número: ')))

if 3 in n:
    print(f'O index do número 3 é: {n.index(3)+1}')
else:
    print('O número 3 não aparece na tupla')
print(f'O número 9 apareceu {n.count(9)}')
print('Os valores pares dgitados foram ', end = '')

for i in n:
    if i %2 == 0:
        print(i, end= ' ')