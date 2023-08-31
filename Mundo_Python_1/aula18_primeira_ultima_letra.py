nome = str(input('Digite seu nome completo: ')).strip().replace(" ","").upper()

print(nome)
print('Em seu nome a letra "A" aparece {} vezes'.format(nome.count("A")))
print('Em qual posição a letra "A" aparece primeiro? {}'.format(nome.find("A",0,len(nome))+1))
print('Em qual posição a letra "A" aparece por ultimo? {}'.format(nome.rfind("A")+1))