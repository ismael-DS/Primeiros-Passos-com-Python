## 2. Peso ideal
print('Digite sua altura')
h = float(input())

print('Digite seu sexo, podendo ser "F" (Feminino) ou "M" (Masculino)')
sexo = input()

if sexo == "M":
 peso = (72.7*h) - 58
else:
 peso = (62.1*h) - 44.7

print('Seu peso ideal é', peso)