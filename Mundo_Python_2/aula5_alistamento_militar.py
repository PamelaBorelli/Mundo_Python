from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

print('Sua idade é {}'.format(idade))
if idade == 18:
    print('Você deve se alistar esse ano')
elif idade < 18:
    saldo = 18-idade
    print('Ainda falta {} anos para seu alisamento'.format(saldo))
    alistamento = ano_atual + saldo
    print('Seu alistamento será em {}'.format(alistamento))
else:
    saldo = idade - 18
    print('Já passou o período de alistamento ha {} anos'.format(saldo))
    alistamento = ano_atual - saldo
    print('Seu alistamento foi em {}'.format(alistamento))
print('--------------------------------------------------------------------------------------------------\n')