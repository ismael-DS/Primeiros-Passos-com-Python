n = int(input('Digite o numero de elementos: '))
prox = ant = 1

print(ant, prox, end = ' ')

for i in range(n-2):
  prox += ant
  ant = prox - ant

  print(prox, end = ' ')