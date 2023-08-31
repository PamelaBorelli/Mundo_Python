from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

print('A idade do(a) atleta é {} anos'.format(idade))

if idade <= 9:
    print('Esse(a) atleta é MIRIM')
elif idade > 9 and idade <= 14:
    print('Esse(a) atleta é INFANTIL')
elif idade > 14 and idade <= 19:
    print('Esse(a) atleta é JUNIOR')
elif idade > 19 and idade <= 25:
    print('Esse(a) atleta é SÊNIOR')
else:
    print('Esse(a) atleta é MASTER')