## 4. Saudação por turno
print('Qual turno você estuda? Podendo ser "M" (Matutino),"V" (Vespertino) ou "N" (Noturno)')
turno = input()

if turno == "M":
  print('Bom dia!')
elif turno == "V":
  print('Boa tarde!')
elif turno == "N":
  print('Boa noite!')
else:
  print('Valor invalido!')