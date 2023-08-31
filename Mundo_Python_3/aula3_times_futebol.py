times = ('Corinthias', 'Vasco', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Chapecoense', 'Atletico', 'Botafogo',
         'Coritiba', 'Avaí', 'Ponte-Preta', 'Flumisense','Bahia')

for t in times:
    print(t, end = ', ')
print('\n')
print('-'*90)
print(f'Os 5 primeiros times são {times[:5]}')
print('-'*90)
print(f'Os 4 ultimos times são {times[-4:]}')
print('-'*90)
print(f'Os times em ordem alfabetica fica {sorted(times)}')
print('-'*90)
print(f'A posição do time da Chapecoense é : {times.index("Chapecoense")+1}')
print('-'*90)



