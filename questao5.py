eleitores = int(input('Digite o numero de eleitores: '))
print('\nCada eleitor pode votar no Alfredo, na Erudina ou no Francisco que são representados pelos numeros 1, 2 e 3 respectivamente')
Alfie = Eru = Chico = 0

for i in range(eleitores):
  voto = int(input('\nDigite seu voto (podendo ser 1, 2 ou 3): '))
  if voto == 1:
    Alfie += 1
  elif voto == 2:
    Eru += 1
  elif voto == 3:
    Chico += 1
  else:
    print('Seu voto foi anulado')

print(f'\nAfredo recebeu {Alfie} votos\nErudina recebeu {Eru} votos\nFrancisco recebeu {Chico} votos')