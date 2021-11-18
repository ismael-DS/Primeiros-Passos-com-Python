def piramide(num): 
  for i in range(1, num+1, 1):
    print('\n')
    for d in range(i):
      print(i, end=' ')
  return

print(piramide(int(input('Digite um numero: '))))