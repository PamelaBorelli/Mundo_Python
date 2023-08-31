from math import factorial

num = int(input('Digite um número: '))
c = num
fatorial = 1
print('Calculando {}! => '.format(num), end = '')
while c > 0:
    print(c,'x ', end ='' )
    fatorial *= c
    c -= 1 
print('{} = {}'.format(c, fatorial))


# f = factorial(num)
# print('{}! = {}'.format(num, f))

