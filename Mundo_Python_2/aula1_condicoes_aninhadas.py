nome = str(input('Digite seu nome: '))

if nome == 'Gustavo':
    print("Que nome bonito")
elif nome == 'Pamela' or nome == 'Ana':
    print('Seu nome é bem normal no Brasil')
elif nome in 'Ana Jessica Maria':
    print('Seu nome é bem normal no EUA')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))

