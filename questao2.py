capital = montante = float(input('Digite seu deposito inicial: '))
juros = float(input('Digite a taxa de juros da sua pupança. Ex: 3 para 3%: '))

for mes in range(1, 25):
  montante += montante * juros / 100
  print('total no', mes, '° mês: %.2f' %montante)

juros = montante - capital

print('O total em 24 meses é de R$%.2f' %montante, 'sendo R$%.2f de juros' %juros)