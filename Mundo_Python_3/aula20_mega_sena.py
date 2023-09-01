from random import randint


print('-'*50)
print('MEGA-SENA')
print('-'*50)


palpites = []
jogos = []
quant_jogos = int(input('Digite a quantidade de jogos q vc quer sortear: '))
tot = 1
while tot <= quant_jogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in palpites:
            palpites.append(num)
            cont += 1
        if cont >= 6:
            break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
    tot += 1
print('-=' *3, f'SORTEANDO {quant_jogos} JOGOS', '-='*3)

for i , j in enumerate(jogos):
    print(f'Jogo {i}: {j}')


