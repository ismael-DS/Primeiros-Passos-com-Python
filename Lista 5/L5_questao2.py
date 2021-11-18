data_nasc = input('Informe uma data de nascimento (dd/mm/aaaa): ').split('/')

data_nasc[0],data_nasc[1],data_nasc[2] = int(data_nasc[0]),int(data_nasc[1]),int(data_nasc[2])

meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

print(f'Data por extenso: {data_nasc[0]} de {meses[data_nasc[1]+1]} de {data_nasc[2]}')