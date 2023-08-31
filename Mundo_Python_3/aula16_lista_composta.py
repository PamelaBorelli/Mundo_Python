lista = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
            
    lista.append(dados[:])
    dados.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar?:[S/N] ')).upper().split()[0]
    if opcao == 'N':
        break
print('-='*60)
print(lista)
print(f'Foram cadastradas {len(lista)}')
print(f'A pessoa mais pesada tem {mai} kg e a mais leve tem {men} kg')

# pesado = []
# leve = []
# for nome, peso in (lista):
#     if peso > 50:
#         pesado.append(nome)
#     else:
#         leve.append(nome)
# print('-='*60)     
# print(f'{pesado} são as mais pesadas e {leve} são as mais leves' )