n = int(input('Digite o numero de alunos na turma: '))
media = 0

for i in range(1, n+1):
  idade = int(input(f'Digite a idade do {i}° aluno: '))
  media += idade/n

if media > 0 and media <= 25:
  print('A turma é jovem')
elif media > 26 and media <= 60:
  print('A turma é adulta')
else:
  print('A turma é idosa')