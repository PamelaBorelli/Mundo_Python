from datetime import date
lista = []
maior = []
menor = []
totmaior = 0
totmenor= 0
ano_atual = date.today().year


for i in range(0,3):
    ano_nasc = int(input('Digite o ano de ascimento da {} pessoa: '.format(i+1)))
    lista.append(ano_nasc)
    idade = ano_atual-ano_nasc
    if idade < 18:
        menor.append(idade)
        totmenor+=1
    else:
        maior.append(idade)
        totmaior +=1

print('oa anos de nascimento são {}, e quem é maior de idade tem {} anos, e quem é menor de idade tem {} anos. No total são {} maiores de idade e {} menores de idade'.format(lista,maior,menor, totmaior,totmenor ))