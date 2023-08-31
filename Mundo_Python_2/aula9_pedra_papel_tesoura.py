from random import randint

print('{:=^60}'.format(' VAMOS JOGAR? '))
print('''Opções:
        [0] Pedra
        [1] Papel
        [2] Tesoura''')
jogador = int(input('Digite sua opção: '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('Você escolheu {} o computador escolheu {}'.format(itens[jogador], itens[computador]))

if jogador == 0 and computador == 1:
    print("Você perdeu")
elif jogador == 0 and computador == 2:
    print('Você ganhou')
elif jogador == 0 and computador == 0:
    print("EMPATE")
elif jogador == 1 and computador == 2:
    print("Você perdeu")
elif jogador == 1 and computador == 0:
    print('Você ganhou')
elif jogador == 1 and computador == 1:
    print("EMPATE")
elif jogador == 2 and computador == 0:
    print("Você perdeu")
elif jogador == 2 and computador == 1:
    print('Você ganhou')
elif jogador == 2 and computador == 2:
    print("EMPATE")
else:
    print('Opção inválida, tente de novo')