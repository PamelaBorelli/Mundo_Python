from random import randint
v = 0
print('VAMOS JOGAR DE PAR OU ÍMPAR?')
while True:
    jogador = int(input('Digite seu número: '))
    computador = int(randint(0,10))
    media = (jogador + computador)
    escolha = ' '
    par = media %2 == 0
    impar = media %2 != 0
    while escolha not in 'PI':
        escolha = str(input('Você escolhe par ou ímpar?[I/P] ')).strip().upper()[0]
    print(f'voce escolheu {jogador}, eu escolhi {computador}. Total {media}', end=' ')
    print(' deu PAR' if media %2 == 0 else 'deu IMPAR')

    if escolha == 'P':
        if media %2 ==0:
            print('Você venceu')
            v +=1
        else:
            print('Você PERDEU')
        break
    elif escolha  == 'I' :
        if media %2 == 1:
            print('Você VENCEU')
            v +=1
            print('='*80)
        else: 
            print('Você PERDEU')
            print('='*80)
            break
        print('vamos jogar novamente.')
print('EU VENCI!!! FIM DE JOGO')