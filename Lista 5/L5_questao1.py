string1 = input('Digite um conteudo para a primeira string: ')
string2 = input('Digite um conteudo para a segunda string: ')

print(f'\nA primeira string contem: "{string1}"\nA segunda string contem: "{string2}"\n')

if len(string1) == len(string2):
  print(f'As strings tem o mesmo comprimento de {len(string1)} caracteres cada uma', end=', ')
  if string1 == string2:
    print('alem de possuirem o mesmo conteúdo')
  else:
    print('embora não possuam o mesmo conteúdo')

else:
  print(f'As strings não tem o mesmo conteúdo nem comprimento, pois a primeira contem {len(string1)} caracteres e a segunda {len(string2)} caracteres\n')

