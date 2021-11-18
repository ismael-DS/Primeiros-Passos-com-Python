import random 

N = int(input("Digite um numero de vezes para rolar o dado: "))
Results = []

for i in range(N):
  Results.append(random.randint(1,6))

print(f'Os resultados ao rolar o dado {N} vezes foram {Results}')