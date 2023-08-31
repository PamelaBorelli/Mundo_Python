nome = str(input('Digite seu nome completo: ')).strip().title()

print('Seu nome tem Silva?: {}'.format('Silva' in nome))
print('Seu nome tem Silva?: {}'.format('SILVA' in nome.upper()))