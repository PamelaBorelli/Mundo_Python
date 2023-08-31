dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)


pessoas = list()

#copia de dados 
pessoas.append(dados[:])
pessoas1 = [['Pedro', 25], ['Maria', 19], ['Jose', 45]]

print(pessoas1)
print(pessoas[0][0])
print(pessoas1[1][1])
print(pessoas1[2][0])
print(pessoas1[1])

