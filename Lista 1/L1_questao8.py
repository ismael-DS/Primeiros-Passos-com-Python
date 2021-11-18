## 8. Adicionando cartão de credito e parcelas
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