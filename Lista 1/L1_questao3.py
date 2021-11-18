## 3. Dados de um trabalhador
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
