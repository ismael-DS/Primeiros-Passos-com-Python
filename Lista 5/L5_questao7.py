num = input('Digite um numero entre 1 e 99: ')

numPrimarios = ('','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove')
Dezenas = ('vinte ','trinta ','quarenta ','cinquenta ','sessenta ','setenta ','oitenta ','noventa ')

if len(num) == 1 or (int(num) > 9 and int(num) < 20):
  extenso = numPrimarios[int(num)]
elif len(num) == 2:
  extenso = Dezenas[int(num[0])-2] + numPrimarios[int(num[1])]
  
print(extenso)