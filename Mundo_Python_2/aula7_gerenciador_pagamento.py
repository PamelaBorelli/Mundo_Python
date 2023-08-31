print('{:=^60}'.format(' BEM-VINDO ÀS COMPRAS '))
valor_compra = float(input('Digite o valor da compra: '))
print('--------------------------------------------------------------------------------------------------\n')
print('''Digite sua opção:
    [1] para dinheiro/cheque
    [2] para caartão à vista
    [3] para 2x no cartão
    [4] para 3x ou mais  no cartão''' )
print('--------------------------------------------------------------------------------------------------\n')

pagamento = int(input('Forma de pagamento: '))
dinheiro = valor_compra - (valor_compra*0.10)
cartao_a_vista = valor_compra - (valor_compra*0.05)
cartao_2x = valor_compra 
cartao_3x = valor_compra + (valor_compra*0.20)

if pagamento == 1:
    print('O valor da sua compra é R${:.2f} e você tem "10%" de desconto. Sua compra sai em R${:.2f}'.format(valor_compra, dinheiro))
elif pagamento == 2:
    print('O valor da sua compra é R${:.2f} e você tem "5%" de desconto. Sua compra sai em R${:.2f}'.format(valor_compra, cartao_a_vista))
elif pagamento == 3:
    parcela = valor_compra / 2
    print('O valor da sua compra é R${:.2f}, a parcela é R${:.2f} e você não tem desconto. Sua compra sai em R${:.2f}'.format(valor_compra, parcela, cartao_2x))
elif pagamento == 4:
    n_parcelas= int(input('Digite o número de parcelas: '))
    parcela = (valor_compra + (valor_compra*0.20)) / n_parcelas
    print('O valor da sua compra é R${:.2f},  a parcela é R${:.2f} e tem acréscimo de "20%" na compra. Sua compra sai em R${:.2f}'.format(valor_compra, parcela, cartao_3x))
else:
    print('Opção inválida, escolha uma opção válida')
