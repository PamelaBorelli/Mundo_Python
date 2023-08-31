vel = float(input('Digite a velocidade: '))

if vel > 100:
    print('Multa gravissima. Pague o valor de 500,00')
elif vel <= 100 and vel >= 80:
    print('Multa grave. Pague o valor de 300,00')
elif vel <= 79 and vel >= 50:
    print('Multa leve. Pague o valor de 100,00')
else:
    print('Você está dentro do limite, PARABENS')