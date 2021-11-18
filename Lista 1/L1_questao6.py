## 6. Media e conceito
print('Digite sua primeira nota:')
N1 = float(input())
print('Digite sua segunda nota:')
N2 = float(input())

media = (N1+N2)/2

if media < 4 and media >= 0:
  print('Sua media numerica é', media, 'e seu conceito é E' )
elif media >= 4 and media < 6:
  print('Sua media numerica é', media, 'e seu conceito é D' )
elif media >= 6 and media < 7.5:
  print('Sua media numerica é', media, 'e seu conceito é C' )
elif media >= 7.5 and media < 9:
  print('Sua media numerica é', media, 'e seu conceito é B' )
elif media >= 9 and media <= 10:
  print('Sua media numerica é', media, 'e seu conceito é A' )
else:
  print('Valor invalido')