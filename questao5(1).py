DataBase = [[None],[None]]
MaiorAltura = 0
MenorAltura = 999
MediaM = 0
MediaF = 0
TotalF = 0
TotalM = 0

for i in range(1, 11):
  DataBase[0].append(float(input(f"Digite a altura da {i} pessoa: ")))
  DataBase[1].append(input(f"Digite o sexo (sendo M ou F) da {i} pessoa: ").upper())
  
  if DataBase[1][-1] == 'M':
    MediaM += DataBase[0][-1]
    TotalM += 1
  if DataBase[1][-1] == 'F':
    MediaF += DataBase[0][-1]
    TotalF += 1

  if DataBase[0][-1] > MaiorAltura:
    MaiorAltura = DataBase[0][-1]
    if DataBase[1][-1] == 'M':
      SexoMaiorAltura = 'masculino'
    if DataBase[1][-1] == 'F':
      SexoMaiorAltura = 'feminino'

  if DataBase[0][-1] < MenorAltura:
    MenorAltura = DataBase[0][-1]
    if DataBase[1][-1] == 'M':
      SexoMenorAltura = 'masculino'
    if DataBase[1][-1] == 'F':
      SexoMenorAltura = 'feminino'

MediaF /= TotalF
MediaM /= TotalM

print(f"\nO individuo mais alto é do sexo {SexoMaiorAltura} e tem {MaiorAltura} metros, enquanto que o mais baixo é do sexo {SexoMenorAltura} e tem {MenorAltura} metros. A media de altura entre as mulheres é de {MediaF} metros e entre os homens é de {MediaM} metros. Foram registrados um total de {TotalF} individuos do sexo masculino e {TotalM} do sexo feminino.")