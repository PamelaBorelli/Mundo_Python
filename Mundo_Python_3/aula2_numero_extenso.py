num_extenso = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito' , 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um númeto de 0 - 20 para ver por extenso: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número { num_extenso[num] }')

