n = 0

while True:
    num = int(input('Digite o número para ver a tabuada: '))
    if num < 0:
        break
    for n in range(0,11):
        print(f'{num} x {n} = {num * n}')
print('PROGRAMA FINALIZADO')
