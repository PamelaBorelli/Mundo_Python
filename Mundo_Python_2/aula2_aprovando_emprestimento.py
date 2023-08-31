casa = float(input('Digite o valor da casa a ser financiada: '))
salario = float(input('Digite seu salario: '))
tempo = int(input('Em quantos anos pretende pagar? '))
prestacao = casa / (tempo*12)
porcao_salario = salario - (salario*0.30)

print(prestacao)
print(porcao_salario)
print(tempo*12)



if prestacao > porcao_salario:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo APROVADO')