num = []
maior = 0
menor = 0

for n in range (0,5):
    num.append(int(input(f'Digite o {n+1}º número: ')))
    if n == 0:
        maior = menor = num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if num[n]< menor:
            menor = num[n]

print(f'Os números digitados foram : {num}')
print(f'O maior número é: {maior}, e ele está nas posições: ', end = ' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i+1}', end = ' ')

print(f'\nO menor número é: {menor}, e ele está nas posições: ', end = ' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i+1}', end = ' ')

# print(f'O maior número {maior} apareceu na posição : {num.index(maior)+1}')
# print(f'O maior número {menor} apareceu na posição : {num.index(menor)+1}')