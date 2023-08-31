# elementos == keys
# conteudo == valor

# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse= True)
# num.insert(2,2)
# #num.pop(2)

# if 4 in num:
#     num.remove()
# else:
#     print('Não existe o número 4 na lista')

# print(num)
# print(len(num))

valores = []
# valores.append(5)
# valores.append(9)
# valores.append(2)

# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))
# print(valores, '\n')



# for c, v in enumerate(valores):
#     print(f'{v} = {c}')

a = [2,3,6,7,8]
# b = a
b = a[:]# faz uma copia de a em b 
b[2] = 4

print(a)
print(b)