from random import randint
from time import sleep

print("VAMOS JOGAR DE ADVINHAR?")
print('==================================================================================================')
num = int(input('Digite um número inteiro de 0 à 10: '))
random_num = randint(0, 10)
print('AGORA É MINHA VEZ. VOU PENSAR EM UM NÚMERO....')
sleep(2)

if num == random_num:
    print('EU ESCOLHI {}, VOCE ESCOLHEU {}'.format(random_num, num))
    print('VOCÊ GANHOU!!!')
    
else:
    print('EU ESCOLHI {}, VOCE ESCOLHEU {}'.format(random_num, num))
    print('VOCÊ PERDEU!!!')