salario = float(input('Digite o valor do salário: '))

if salario <= 1250:
    print('O salario com aumento é: {:.2f}'.format(salario*1.15))
else:
    print('O salario com aumento é: {:.2f}'.format(salario*1.10))