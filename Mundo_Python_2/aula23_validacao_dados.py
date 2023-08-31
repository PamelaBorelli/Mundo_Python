genero = str(input('Digite o gênero da pessoa:[F/M] ')).strip().upper()[0]
feminino = masculino = 0

while genero == 'F' or genero == 'M':
    genero = str(input('Digite o gênero da pessoa:[F/M] ')).strip().upper()[0]
    if genero == 'F':
        feminino += 1
    if genero == 'M': 
        masculino +=1
else:
    print('Informação inválida, digite novamente.')
print('Você digitou {} feminino e {} masculino'.format(feminino, masculino))

# while genero not in 'MmFf':
#     genero= str(input('Informação inválida, digite novamente: ')).strip().upper()[0]
# print('Genero {} registrado com sucesso'.format(genero))