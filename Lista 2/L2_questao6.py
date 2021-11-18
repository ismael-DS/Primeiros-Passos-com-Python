##6. Sistema de vendas
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