print('digite o numero da questão')
question = input()

## 1. calcular area de um circulo
if question == '1':

 print('Qual o raio do circulo?')
 R = int(input())
 Area_PI = R * R
 Area = R * R * 3.14

 print ('A area do circulo é', Area_PI, 'π ou', Area, 'se considerarmos π como 3,14')

## 2. Peso ideal
elif question == '2':

 print('Digite sua altura')
 h = float(input())

 print('Digite seu sexo, podendo ser "F" (Feminino) ou "M" (Masculino)')
 sexo = input()

 if sexo == "M":
  peso = (72.7*h) - 58
 else:
  peso = (62.1*h) - 44.7

 print('Seu peso ideal é', peso)

## 3. Dados de um trabalhador
elif question == '3':
 print('Digite o valor ganho por hora de trabalho:')
 salario_hora = float(input())

 print('Digite o numero de horas trabalhadas no mês:')
 hora_mes = int(input())

 salario_bruto = salario_hora * hora_mes
 INSS = (salario_bruto * 8) / 100
 IR = (salario_bruto * 11) / 100    
 Sindicato = (salario_bruto * 5) / 100
 salario_liq = salario_bruto - (INSS + IR + Sindicato)

 print(' Salario bruto: R$', salario_bruto, '\n INSS: R$', INSS, '\n Imposto de renda: R$', IR, '\n Sindicato: R$', Sindicato, '\n Salario Liquido: R$', salario_liq)  

## 4. Saudação por turno
elif question == '4':
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

## 5. Classificar triangulo
elif question == '5':

 print('Digite o L1 do triangulo')
 L1 = int(input())
 print('Digite o L2 do triangulo')
 L2 = int(input())
 print('Digite o L3 do triangulo')
 L3 = int(input())

 if L1 == L2 == L3:
   print('Triângulo equilátero')
 elif L1 == L2 or L1 == L3 or L2 == L3:
   print('Triângulo isóceles')
 else:
   print('Triângulo escaleno') 

## 6. Media e conceito
elif question == '6':
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

## 7. Desconto
elif question == '7':
  print('Digite o valor da compra:')
  valor = float(input())
  print('Digite a forma de pagamento, podendo ser "D" (Dinheiro) ou "C" (Cheque)')
  pagamento = input()
  
  pagamento_desc = valor - (valor/10)

  if valor >= 100 and pagamento == "D":
   print('Total a pagar: R$', pagamento_desc)
  else:
    print('Total a pagar: R$', valor)

## 8. Adicionando cartão de credito e parcelas
elif question == '8':
  print('Digite o valor da compra:')
  valor = float(input())
  print('Digite a forma de pagamento, podendo ser "D" (Dinheiro), "CA" (Cartão) ou "CH" (Cheque)')
  pagamento = input()
  
  pagamento_desc = valor - (valor/10)

  if pagamento == "CA":
    print('Digite a função Debito ("D") ou Credito ("C")')
    funcao = input()
    if funcao == "C": 
      print('Digite o numero de parcelas, podendo dividir de 1 a 3 vezes no cartão')
      parcelas = int(input())
      

  if valor >= 100 and pagamento == "D":
   print('Total a pagar: R$', pagamento_desc)
  elif pagamento == "CA" and funcao == "C":
    print('Total a pagar: R$', valor/parcelas) 
  else:
    print('Total a pagar: R$', valor)