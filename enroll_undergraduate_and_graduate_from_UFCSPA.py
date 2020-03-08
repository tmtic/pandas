import pandas as pd
from os import path, system
from sys import platform

if 'win' in platform:
	system('cls')
else:
	system('clear')
	
try:
	arc = path.split(path.abspath(__name__))[0] + path.sep 
	df = pd.read_csv(arc+'matriculas.csv', delimiter=';')
	filtro = df.loc[(df['ANO_INGRESSO'] == 2020) & (df['NOME_CURSO_DIPLOMA'] == 'Curso de Medicina')]	
	filtro = filtro.to_dict('dict')
	filtro = pd.DataFrame(filtro)
	 
	filtro.to_csv(arc+'matriculas_novo.csv', index=False)
	print("Successfull generated!")
	
except Exception as err:
	print(err)