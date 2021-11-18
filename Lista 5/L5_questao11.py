def digit(num):
  if type(num) != int:
    return print('Error: o parametro de "digit()" deve ser um numero inteiro')
  num = str(num)
  total = 0

  for caractere in num:
    total += 1

  return total

print(digit(int(input('Digite um numero inteiro: '))))