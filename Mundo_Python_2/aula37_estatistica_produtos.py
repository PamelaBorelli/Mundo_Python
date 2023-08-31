valor_compra = 0
mais_caro = 0
mais_barato = 0
nome_barato = ' '
cont = 0


print("-"*80)
print('{:^80}'.format('LOJA DA PAMELA'))
print("-"*80)

while True:
    nome_produto= str(input('Qual o nome do poduto?: '))
    preco = 0
    preco = float(input('Digite o valor: R$ '))
    valor_compra += preco
    cont +=1
    if preco > 1000:
        mais_caro += 1
    
    if cont == 1 or preco < mais_barato: 
        mais_barato = preco
        nome_barato = nome_produto

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja adicionar mais algum produto?[S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print('\n')
print('{:-^80}'.format('FIM DA COMPRA'))
print(f'O valor da compra foi {valor_compra:.2f},  {mais_caro} produtos custam mais de R$1.000,00, o produto mais barato é {nome_barato} que custou R$ {mais_barato:.2f}')