from time import sleep

valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))

print('*'*100,'\n')
print('''O que você quer fazer com esses números?
      [1] somar
      [2] multiplicar
      [3] dizer qual é o maior
      [4] digitar novos números
      [5] sair do programa''')


opcao = 0
while opcao != 5:
    opcao = int(input('Digite uma opcao do menu: '))
    if opcao == 1:
        soma = valor1 + valor2
        print('{} + {} = {}'.format(valor1, valor2, soma))
        print('*'*100,'\n')
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print('{} x {} = {}'.format(valor1, valor2, multiplicacao))
        print('*'*100,'\n')
    elif opcao == 3:
        if valor1 > valor2:
            print("{} é maior que {}".format(valor1, valor2))
            print('*'*100,'\n')
        else:
            print("{} é maior que {}".format(valor2, valor1))
            print('*'*100,'\n')
    elif opcao == 4:
        print('Digite novos valores: ')
        valor1 = int(input('Digite o 1º valor: '))
        valor2 = int(input('Digite o 2º valor: '))
        print('*'*100,'\n')
    elif opcao == 5:
        print('Saindo do programa...')
        sleep(2)
        print('TCHAU!!!!')
    else:
        print('Opcão inválida, digite nova opcao: ')