num = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
decimo = num+(10-1)*razao

for i in range(num, decimo+1, razao):
    print('{}'.format(i), end = '-> ')
print('ACABOu')