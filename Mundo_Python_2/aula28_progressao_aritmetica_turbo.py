print('Vamso calcular uma PA')
num = int(input('Digite um número: '))
razao = int(input('Digite razao da PA: '))
c = 1
termo = num
mais = 10
total = 0

while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(termo), end = '')
        c +=1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais? '))
    termo += razao
print('Fim do programa. Foram mostrados {} termos'.format(total))