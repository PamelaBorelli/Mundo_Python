listagem = ('Lápis', 1.75,
            'borracha', 2.35,
            'caneta', 2.65,
            'mochile', 125.00,
            'livro', 56.00,
            'estojo', 18.70)


# for pos, item in enumerate(listagem):
#     print(pos, item)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(0,len(listagem)):
    if pos %2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R$ {listagem[pos]:>5}')

print('-'*40)