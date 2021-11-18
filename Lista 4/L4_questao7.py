frase = input("digite uma frase: ")

while frase != '1':
  dicionario = {}

  for letra in frase:
    if letra not in dicionario:
      dicionario[letra] = 1
    elif letra in dicionario:
      dicionario[letra] += 1

  print(dicionario)
  frase = input("digite uma frase: ")