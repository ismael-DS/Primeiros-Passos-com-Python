##1. Numeros impares multiplos de 3
num = 1
mult = 0
soma = 0

while mult >= 0:
  soma += mult
  mult = num * 3
  num += 2
  if mult >= 500:
    break

print(f'A soma dos numeros impares multiplos de 3 no intervalo (1,500) é igual a {soma}')