##5. Calculadora de dividas
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