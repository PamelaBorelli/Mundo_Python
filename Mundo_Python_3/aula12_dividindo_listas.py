lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar:[s/n] ')).upper().split()[0]
    if opcao == 'N': 
        break

for i in lista:
    if i%2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
            
print(f'A lista digitada é: {lista}')
print(f'Os números pares são: {lista_par}')
print(f'Os números impares são: {lista_impar}')