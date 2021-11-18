##2. Maior, menor e soma dos numeros digitados
soma = 0
num = menor = maior = float(input('Digite um numero: '))

while num != -1:
  soma += num
  num = float(input('Digite um numero: '))

  if num > maior:
    maior = num
  if num < menor:
    menor = num
    
print(f'Maior valor digitado: {maior}\nMenor valor digitado: {menor}\nSoma de todos os valores digitados: {soma}')