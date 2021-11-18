resultado = base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

for i in range(expoente-1):
  resultado *= base
  
print(resultado)