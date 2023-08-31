from random import randint
print('*'*100)
print('''Olá!!!! Sou seu computador!
Pensei em um número, você consegue adivinhar?''')
print('*'*100,'\n')

# num = int(input('Digite um número de 0 à 10: '))
# computador = randint(0,10)
# palpites = 0

# while num != computador:
#     palpites +=1
#     if num < computador:
#         print('O número que eu escolhi é maior')
#     else:
#         print('O número que eu escolhi é menor')
#     num = int(input('Digite novamente: '))
# print('*'*100,'\n')
# print('Foram {} palpites. Você digitou {}, eu escolhi {}'.format(palpites, num, computador))
# print('Você acertou!!! PARABÉNS')
# print('*'*100,'\n')

computador = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    if palpites < computador:
       print('O número que eu escolhi é maior')
    else:
       print('O número que eu escolhi é menor')
    # palpites = int(input('Digite novamente: '))
print('*'*100,'\n')
print('VOCÊ ACERTOU')
print('Foram {} palpites'.format(palpites))
print('*'*100,'\n')

