# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         num = int(input('Digite um valor: '))
#         linha.append(num)
#     matriz.append(linha)
# print(matriz)

matriz = [ [0,0,0], [0,0,0], [0,0,0] ]
pares = mai = col = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = (int(input(f'Digite um valor para [{i}, {j}]: ')))
print()
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end ='')
        if matriz[i][j]%2 == 0:
            pares += matriz[i][j]
    print()  
    
for i in range(0,3):
    col += matriz[i][2]  
    
for j in range(0,3):
    if matriz[1][j] > mai:
        mai = matriz[1][j]
        

print(pares)
print(col)       
print(mai)
        



