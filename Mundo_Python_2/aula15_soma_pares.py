soma = 0
num = []

for i in range(0,6):
    num = int(input("digite o {}º número: ".format(i+1)))
    if num% 2 ==0 :
        soma += num
        # print(soma)
print('A soma de dos números pares foi {}'.format(soma))