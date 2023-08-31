''''
colculando a hipotenusa
'''

from math import sqrt, hypot

cateto_oposto= float(input('Digite o valor do cate oposto: '))
cateto_adjacente= float(input('Digite o valor do cate ajacente: '))
hipotenusa = ((cateto_adjacente**2) +(cateto_oposto**2))

print("A hipotenusa é {:.2f}".format(sqrt(hipotenusa)))
print("A hipotenusa é {:.2f}".format(hypot(cateto_adjacente, cateto_oposto)))