pesos=[]
maior_peso = 0
menor_peso = 0

for pessoas in range(0,4):
    lista = float(input('Digite o peso da {}º pessoa: '.format(pessoas+1)))
    pesos.append(lista)
    
    if pessoas == 1:
        menor_peso = lista
        maior_peso = lista
    else:
        if lista < menor_peso:
            menor_peso = lista       
        if lista > maior_peso:
            maior_peso = lista
        
print('Os pesos foram: {}. O maior peso é {}Kg e o menor peso é {}kg'.format(pesos, maior_peso, menor_peso))