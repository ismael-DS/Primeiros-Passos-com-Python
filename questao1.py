fator1 = int(input('Digite um numero entre 1 e 10 para ver a tabuada dele: '))

if fator1 > 10 or fator1 < 0: 
  print('apenas numeros entre 1 e 10')
else:
  print(f'A tabuada de {fator1} é: ')
  
  for fator2 in range(1,11):
    print(f'{fator1} X {fator2} = {fator1 * fator2}')    