num = int(input("digite um número para ver sua tabuada: "))

for i in range(0,10):
    tabuada = num *(i+1)
    print('A tabuada de {} X {} = {}'.format(num, i, tabuada))

# for i in range(0,10):
#     print('A tabuada de {} X {} = {}'.format(num, i, num*i))