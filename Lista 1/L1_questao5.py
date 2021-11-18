## 5. Classificar triangulo
print('Digite o L1 do triangulo')
L1 = int(input())
print('Digite o L2 do triangulo')
L2 = int(input())
print('Digite o L3 do triangulo')
L3 = int(input())

if L1 == L2 == L3:
 print('Triângulo equilátero')
elif L1 == L2 or L1 == L3 or L2 == L3:
 print('Triângulo isóceles')
else:
 print('Triângulo escaleno') 