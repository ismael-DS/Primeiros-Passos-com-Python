import math

N = int(input('Digite o numero de pontos a serem analisados: '))
pontos = []
distancias = []
media = 0
distanciaMinima = 9999999999
distanciaMaxima = -9999999999

for i in range(1, N+1):
    x = float(input(f'\nDigite a coordenada X do {N}° ponto: '))
    y = float(input(f'Digite a coordenada Y do {N}° ponto: '))

    coordenadas = (x, y)
    pontos.append(coordenadas)

for b in range(N):
    ponto = pontos[b]

    for c in range(b+1, N):
        distancia = math.sqrt((pontos[c][0]- ponto[0]) ** 2 + (pontos[c][1] - ponto[1]) ** 2)
        distancias.append(distancia)
        
        if distancia > distanciaMaxima:
         distanciaMaxima = distancia
        if distancia < distanciaMinima:
         distanciaMinima = distancia
        media += distancia

media = media / len(distancias)

print(f'\nA distância máxima é {distanciaMaxima:.2f}, enquanto a mínima é {distanciaMinima:.2f} e a média é {media:.2f}')