#!/bin/python3 

# INTRODODUCCION A PANDAS

import pandas;

# Obteniendo datos desde un archivo...
data = pandas.read_csv("./alumnos.csv");

# conceptos basicos:
#     series: conjuntos de datos unidimensional (en math: vector, en db: fila)
#     dataframe: conjunto de datos bidimensional (en math: matriz, en db: tabla) 

print(data)

# Informacion del DataFrame
print("")
print("-"*25)
print("")
print(data.info())

# Descripcion estadistica del DataFrame
print("")
print("-"*25)
print("")
print(data.describe())

# Filtrados
print("")
print("-"*25)
print("")
print(data[data.edad > 31])

# Ordenamientos
print("")
print("-"*25)
print("")
print(data.sort_values(by="edad"))

# Agrupamiento
print("")
print("-"*25)
print("")
print(data.groupby("curso")["edad"].mean())

# salida en archivo de texto CSV
data.to_csv("./alumnos_2.csv", index=False)