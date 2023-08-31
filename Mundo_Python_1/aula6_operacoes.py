# num = int(input('Digite um número: '))

# print('Seu dobro é {}'.format(num*2))
# print('Seu triplo é {}'.format(num*3))
# print('Sua raiz quadrada é {:.2f}'.format(num**(1/2)))


larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

print("A área da parede é {}".format(larg*alt))
print('para pintar essa parede você precisa de {} litros de tinta'.format((larg*alt)/2))