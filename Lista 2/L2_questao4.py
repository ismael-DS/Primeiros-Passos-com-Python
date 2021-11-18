##4. Divisão inteira e resto 
numA = int(input('Digite o divisor: '))
numB = int(input('Digite o dividendo: '))
rest = 0
result = 0

while numA > 0:   
  if (numA - numB) < 0:
    rest = numA
    break
  else:
    numA = numA - numB
  result += 1

print(f'O resultado da divisão é {result} e o resto da operação é {rest}')