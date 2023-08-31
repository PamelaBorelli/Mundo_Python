idade = 0
homens= 0
mulheres = 0
cont = 0
while True:
    idade = int(input('Qual a idade: '))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Digite o genero:[F/M]: ')).strip().upper()[0]
    if idade > 18:
        cont +=1
    if genero == 'M':
        homens +=1
    if genero == 'F' and idade < 20: 
            mulheres +=1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar cadastrando?[S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('FIM DO PROGRAMA....saindo')
print(f'{cont} pessoas tem mais de 18 anos, {homens} homens foram cadastrados, {mulheres} mulheres tem menos de 20 anos')
