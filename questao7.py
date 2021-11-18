n = int(input("Verificar numeros primos ate: "))
primo = True

for i in range(2,n):
  if (n % i == 0):
    primo = False

if primo == False  or n == 0 or n == 1:
  print('não é primo')
if primo == True:
  print("É primo")