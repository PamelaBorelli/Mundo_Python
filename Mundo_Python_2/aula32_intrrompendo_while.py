# cont = 1

# while cont <= 10:
#     print(cont, ' ', end='')
#     cont += 1
# print('Acabou')

n = 0
s = 0
# while n != 999:
#     n = int(input('Digite um número: '))
#     if n != 999:
#         s += n
# print(s)

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(s)