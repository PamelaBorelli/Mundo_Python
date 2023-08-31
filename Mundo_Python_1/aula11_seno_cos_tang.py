import math

ang = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O valor do seno é {:.2f}, cosseno {:.2f}, tangente {:.2f} para o ângulo {:.2f}'.format(seno, cos, tang, ang))