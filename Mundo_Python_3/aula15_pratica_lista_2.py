# teste = []

# teste.append('Pamela')
# teste.append(36)

# print(teste)

# galera = []
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['Joao', 34], ['Pedro', 56], ['Maria', 34]]
# print(galera[0])
# print(galera[0][0])

# for p in galera:
#     print(p)
#     print(f'{p[0]} tem {p[1]} anos')
    

galera = []
dados = []
totmai = totmen = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
    
print(galera)

for p in galera:
    if p[1] >= 21:
        totmai +=1
        print(f'{p[0]} é maior de idade')
    else:
        totmen += 1
        print(f'{p[0]} é menor de idade')
print(f'{totmai} são maiores de idade, {totmen} são menores de idade')