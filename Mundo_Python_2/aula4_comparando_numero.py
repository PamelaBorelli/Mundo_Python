n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('--------------------------------------------------------------------------------------------------')
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}'.format(n1, n2))
else:
    print('{} é igual que {}'.format(n1, n2))
print('--------------------------------------------------------------------------------------------------\n')