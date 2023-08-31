nome = str(input('Digite seu nome completo: ')).strip()

print("seu nome tem {} letras".format(len(nome)-nome.count(' ')))
print("seu nome em maiusculo é {}".format(nome.upper()))
print("seu nome em minusculo é {}".format(nome.lower()))
print("seu nome sem espaço fica {}".format(nome.replace(" ","")))
print("seu primeiro nome tem {} letras".format(nome.find(' ')))
separa = nome.split()
print("seu primeiro nome {}, tem {} letras".format(separa[0], len(separa[0])))
