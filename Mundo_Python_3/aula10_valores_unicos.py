num = int(input('Quantos números voce quer adicionar na lista: '))
lista_num = []

for i in range(0,num):
    n = (int(input(f'Digite o {i+1}º número: ')))
    if i == 0 or n > lista_num[-1]:
        lista_num.append(n)
        print('Adicionado no final da lista ')
        # for i in len(lista_num):
        #     if n in len(lista_num): 
        #         lista_num.pop(i)
        #         print(f'Não é possível adicionar números repetidos na lista {i}')
    else:
        pos = 0
        while pos <len(lista_num):
            if n <= lista_num[pos]:
                lista_num.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista_num)

