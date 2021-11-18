##3. População de um país ultrapassar outro
population_x = 70000
population_y = 180000
years = 0

while population_x < population_y:
  years += 1
  population_x *= 1.035
  population_y *= 1.015

print(f'Foram necessarios {years} anos para a população do país X igualar ou ultrapassar a população do país Y')
