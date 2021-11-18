## 7. Desconto
print('Digite o valor da compra:')
valor = float(input())
print('Digite a forma de pagamento, podendo ser "D" (Dinheiro) ou "C" (Cheque)')
pagamento = input()
  
pagamento_desc = valor - (valor/10)

if valor >= 100 and pagamento == "D":
 print('Total a pagar: R$', pagamento_desc)
else:
 print('Total a pagar: R$', valor)
