num = int(input('Digite um número: '))
tot=0
for i in range(1,num+1):
    if num%i==0:
        print('\033[m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
if tot ==2:
    print('\nO número {} é primo'.format(num))
else:
    print('\nO número {} não é primo'.format(num))
