frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''
invertido2 = junto[::-1]

print('A frase digitada foi: {}\n'.format(frase))

# for letra in range (len(junto) -1,-1,-1):
#     invertido += junto[letra]
if invertido2 == junto:
    print('A frase é um palindromo')
else:
    print('A frase NÃO é um palindromo')

print(junto, invertido2)


