dis = float(input('Qual a distancia da sua veiagem?: '))

if dis <= 200:
    print('O valor da sua viagem é: R${:.2f}'.format(dis*0.5))
else:
    print('O valor da sua viagem é: R${:2.f}'.format(dis*0.45))

