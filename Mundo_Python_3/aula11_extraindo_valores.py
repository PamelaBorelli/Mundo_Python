lista = []


while True:
    lista.append(int(input('Digite um número: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar:[s/n] ')).upper().split()[0]
    if opcao == 'N': 
        break
   
print('-='*45)
print(f'Você digitou os números: {lista}, foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')