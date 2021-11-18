def sinal(num):
  if num > 0:
    signal = 'P'
  elif num < 0:
    signal = 'N'
  elif num == 0:
    signal = 'O numero 0 não é positivo nem negativo'
    
  return signal

print(sinal(int(input("Digite um numero: "))))