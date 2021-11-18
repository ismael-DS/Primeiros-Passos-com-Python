matriz = [[None]*3 for i in range(0,3)]

for i in range(3):
  for j in range(3):
    matriz[i][j] = int(input('Digite o valor do elemento [%d][%d]: ' % (i, j)))

elementoAnterior = matriz[0][1]
matriz[0][1] = matriz[1][0]
matriz[1][0] = elementoAnterior
elementoAnterior = matriz[2][1]
matriz[2][1] = matriz[1][2]
matriz[1][2] = elementoAnterior

print("\nTrocando a linha 2 pela coluna 2 e vice-versa temos:\n")
for i in range(3):
  print(matriz[i])