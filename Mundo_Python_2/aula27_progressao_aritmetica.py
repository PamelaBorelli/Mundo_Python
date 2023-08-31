print('Vamso calcular uma PA')
num = int(input('Digite um número: '))
razao = int(input('Digite razao da PA: '))
c = 1
termo = num
pa = 0

# PA = a1 + (n – 1). r
while c <= 10:
    print('{} -> '.format(termo), end = '')
    c +=1
    termo += razao
    pa += termo
print(pa)
