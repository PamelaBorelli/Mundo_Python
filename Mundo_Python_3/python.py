import numpy
import math
import statistics
from collections import Counter

n = (120, 250, 250,	251, 251, 785,	458, 124, 245, 125,
201, 365,	654,	568,	251,	365,	145,	896,	145,	256,
896,	785,	456,	256,	123,	154,	452	,258,	145	,695,
145,	254,	654,	563,	562,	456,	125,	145,	258,	145,
145	,895,	145,	785,	458	,800,	900,	400,	500,	365,
254,	365,	154,	215,	458,	254,	258,	145	,369,	547,
589,	698,	698,	789,	544,	456,	356,	548,	569, 598)

ordenado = sorted(n)
print(ordenado)
somado = sum(n)/70
print(somado)
mediana = numpy.median(n)
print(mediana)

moda = statistics.mode(n)
print(moda)

dados = Counter(ordenado)
print(dados)

