def charCount(frase):
  while frase != '1':
    dicionario = {}
    
    for letra in frase:
      if letra not in dicionario:
        dicionario[letra] = 1
      elif letra in dicionario:
        dicionario[letra] += 1
      
    return dicionario

print(charCount(input('')))    