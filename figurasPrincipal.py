import pandas as pd
from funciones import triangulo, rectangulo, circulo	#llama las funciones definidas en funciones.py

dataFile = pd.read_csv("figuras.csv", sep=" ")	#lee el archivo que contiene las medidas de las figuras

print("Procesando figuras ...\n")

for index, row in dataFile.iterrows(): 		#itera por cada fila

	if row['FIGURA'] == 't':		#decide qué formula usar según la figura
		area = triangulo(row['MEDIDA1'], row ['MEDIDA2'])
	elif row['FIGURA'] == 'r':
		area =rectangulo(row['MEDIDA1'], row ['MEDIDA2'])
	elif row['FIGURA'] == 'c':
		area =circulo(row['MEDIDA1'])
	print(f"Fila {index}: FIGURA ={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")	
	print(f"Fila {index}: Area:{area}") #imprime el resultado
