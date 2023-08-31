opcao = 'S'
maior = 0
menor = 0
media = 0
num = 0
soma = 0
quant = 0
while opcao == 'S':
    num = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar?[S/N] ')).strip().upper()
    soma += num
    quant += 1
    if quant == 1: 
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if menor > num:
            menor = num
    while opcao not in 'NS':
        print('Digite uma opção válida [S/N]')
        opcao = str(input('Deseja continuar?[S/N] ')).strip().upper()
media = soma / quant
print('O maior número foi {}, o menor número foi {}, a média entre os números digitados foi {:.2f}'.format(maior, menor, media))