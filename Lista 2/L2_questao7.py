##7. Raiz quadrada
p = 2.0
b = 0.0
n = float(input('digite o numero para calcular a raiz quadrada: '))

while (abs(b-p) > 0.0001):
  b = p
  p = (b + (n/b))/2

print('A raiz de %.2f'  %n, 'é aproximadamente: %.2f' %b)