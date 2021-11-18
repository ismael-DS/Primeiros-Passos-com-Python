## Jogo de forca
import random

palavra = random.choice(open("palavras.txt","r").readline().split(' '))
count = 0
tentativas = []

while True:
  print('\nA palavra é ',end='')
  for letra in palavra:
    if letra in tentativas:
      print(letra,end='')
    else:
      print('_',end='')
      WIN = False
  
  if WIN == True:
    print('\nPARABENS, VOCÊ GANHOU O JOGO')
    break

  WIN = True

  tentativas.append(input('\nDigite uma letra: ').upper())

  if tentativas[-1] not in palavra:
    count += 1
    if count == 6:
      print('\nVocê errou pela 6° vez e foi enforcado\n\nGAME OVER')
      break
    else:
      print(f'\n-> Você errou pela {count} vez, tente novamente')