Vetor1 = [None]*5
Vetor2 = [None]*5
Vetor3 = []

Vetor1[0], Vetor1[1], Vetor1[2], Vetor1[3], Vetor1[4] = input("Digite 5 valores pro Vetor 1 separando com espaço: ").split(" ")

Vetor2[0], Vetor2[1], Vetor2[2], Vetor2[3], Vetor2[4] = input("Digite 5 valores pro Vetor 2 separando com espaço: ").split(" ")

for i in range(5):
  Vetor3.append(Vetor1[i])
  Vetor3.append(Vetor2[i])

print(Vetor3)