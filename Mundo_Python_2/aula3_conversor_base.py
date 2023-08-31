num = int(input('Digite um número inteiro: '))
print('--------------------------------------------------------------------------------------------------\n')
print('''Digite sua opção:
    [1] para binário
    [2] para octal
    [3] para hexadecimal''' )
print('--------------------------------------------------------------------------------------------------\n')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('{} convertudo para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertudo para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertudo para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
print('--------------------------------------------------------------------------------------------------\n')