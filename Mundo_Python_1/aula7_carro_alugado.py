'''
Escreva um progrma qu pergunte a quantdade de km percorrido por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro
custa R$60,00 por dia e R$ 0,15 por km rodado

'''

dias = int(input('Digite a quantidade de dias que você ficou com o carro: '))
km = float(input('Digite a quantidade de km que o carro rodou: '))

preco = ((dias*60) + (km*0.15))

print('O valor da diária é: R${:.2f}'.format(preco))