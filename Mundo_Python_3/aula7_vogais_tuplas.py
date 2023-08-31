palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')


# for letras in range(0, len(palavras)):
#     if letras in 'AEIOU':
#         print(f'{palavras} as vogais são: {letras}')

for p in palavras:
    print(f'\nNa palavra "{p}" temos ', end = '')
    for letras in p:
        if letras in 'AEIOU':
            print(letras.lower(), end = ' ')
