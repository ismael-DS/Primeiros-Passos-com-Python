question = input('Digite o numero da questão desejada: ')

##1. Numeros impares multiplos de 3
if question == '1':
  num = 1
  mult = 0
  soma = 0

  while mult >= 0:
    soma += mult
    mult = num * 3
    num += 2
    if mult >= 500:
      break

  print(f'A soma dos numeros impares multiplos de 3 no intervalo (1,500) é igual a {soma}')

##2. Maior, menor e soma dos numeros digitados
if question == '2':
  soma = 0
  num = menor = maior = float(input('Digite um numero: '))

  while num != -1:
    soma += num
    num = float(input('Digite um numero: '))

    if num > maior:
      maior = num
    if num < menor:
      menor = num
    
  print(f'Maior valor digitado: {maior}\nMenor valor digitado: {menor}\nSoma de todos os valores digitados: {soma}')

##3. População de um país ultrapassar outro
if question == '3':
  population_x = 70000
  population_y = 180000
  years = 0

  while population_x < population_y:
    years += 1
    population_x *= 1.035
    population_y *= 1.015

  print(f'Foram necessarios {years} anos para a população do país X igualar ou ultrapassar a população do país Y')

##4. Divisão inteira e resto 
if question == '4':
  numA = int(input('Digite o divisor: '))
  numB = int(input('Digite o dividendo: '))
  rest = 0
  result = 0

  while numA > 0:   
    if (numA - numB) < 0:
      rest = numA
      break
    else:
      numA = numA - numB
    result += 1

  print(f'O resultado da divisão é {result} e o resto da operação é {rest}')

##5. Calculadora de dividas
if question == '5':
  divida = restante = float(input("Dívida: "))
  juros_mensal = float(input("Juros (Ex: 3 para 3%): "))
  pagamento_mensal = float(input("Pagamento mensal: "))
  total = 0 
  count = 0

  if (divida * (juros_mensal/100) > pagamento_mensal):
    print("Os juros da sua divida são superiores ao pagamento mensal, portanto ela nunca vai ser paga :-/")
  else:
    juros_pago = 0

    while restante > 0:
      juros = restante * juros_mensal / 100
      juros_pago += juros
      restante += juros - pagamento_mensal
      count += 1
  total = juros_pago + divida
  print ('Você pagara sua divida em', count,' meses, pagando um total de %.2f' %total, 'total sendo %.2f de juros.' %juros_pago)

##6. Sistema de vendas
if question == '6':
  total = 0
  code = 'x'

  while True:
    code = input('1 - 5.50\n2 - 2.30\n3 - 4.75\n4 - 6.80\n5 - 9.30\nDigite o codigo do Produto desejado de acordo com a tabela: ')

    if code == '0':
      break
    elif code == '1':
      amount = int(input('Digite a quantidade do produto desejado:'))
      total = (5.50 * amount) + total
    elif code == '2':
      amount = int(input('Digite a quantidade do produto desejado:'))
      total = (2.30 * amount) + total
    elif code == '3':
      amount = int(input('Digite a quantidade do produto desejado:'))
      total = (4.75 * amount) + total
    elif code == '4':
      amount = int(input('Digite a quantidade do produto desejado:'))
      total = (6.80 * amount) + total
    elif code == '5':
      amount = int(input('Digite a quantidade do produto desejado:'))
      total = (9.30 * amount) + total
    else:
      print('Codigo inválido')

  print(f'O total a ser pago é de R${total} reais')

##7. Raiz quadrada
if question == '7':
  p = 2.0
  b = 0.0
  n = float(input('digite o numero para calcular a raiz quadrada: '))

  while (abs(b-p) > 0.0001):
    b = p
    p = (b + (n/b))/2

  print('A raiz de %.2f'  %n, 'é aproximadamente: %.2f' %b)