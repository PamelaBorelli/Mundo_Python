cont = 0
soma= 0
# num = 0
# while num != 999:
#     num = int(input('Digite um número para somar, ou [999] para parar: '))
#     if num != 999:
#         cont +=1
#         soma += num
#     else:
#         print('Fim')
# print('Você digitou {} números e a soma deles é {}'.format(cont, soma))
num = int(input('Digite um número para somar, ou [999] para parar: '))
while num != 999:
    cont +=1
    soma += num
    num = int(input('Digite um número para somar, ou [999] para parar: '))
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))