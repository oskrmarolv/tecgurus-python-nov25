#!/bin/python3

"""
"""

"""
IDENTACION: la definicion de bloques de codigo

PEP:
	* Los bloques de codigo se estructuran a partir de la indentacion de codigo y no a traves de otros elementos como las "{" "}"
	* El espacio es de 4 caracteres para la indentacion
	* La longitud maxima en linea de codigo sera de 79 caracteres
	* Identacion a traves del caracter de tabulacion (\\t)
"""

# valores que podemos encontrar monitoreando recursos de un equipo de computo
estado = "oculto"
cpu = 40
ram = 78

# Sentencia "if-elif-else" (decision)
# if OPERACION_BOOLEANA:

if cpu > 75:
	if ram > 50:
		print("El equipo esta sobre cargado.")
	else:
		print("Necesito revision.")
elif cpu > 40:
	print("Necesito revision.")
else:
	print("Equipo optimo")

# sentencia "for" (repeticion)
# for VALOR in ITERABLE:
for x in range(10):
	if x == 5:
		continue
	print("for", x)

# sentencia "while" (repeticion)
# while VALOR_BOOLEANO:

indice = 0
while indice < 10:
	print("while", indice)
	#indice = indice + 1 	
	indice += 1 				# no existe operadores de incremento/decremento
	# indice *= 1
	# indice /= 1
	if indice == 8:
		break

# sentencia "pass" "continue" "break"
# en sentencias de repeticion
# 	continue 		salta al siguinte ciclo de la iteracion
# 	break 			termina la iteracion por completo
#	pass			comodin para completar indentar

if True == True:
	pass

print("end..")


# sentencia "match"	(decision)
#  solo disponible a partir de version 3.10 de Python

match estado:
	case "activo":
		print("el equipo esta activo")
	case "mantenimiento":
		print("el equipo esta mantenimiento")
	case _:
		print("el equipo esta fuera de servicio")

# antes de verion 3.10...
if estado == "activo":
	pass
elif estado == "mantenimiento":
	pass
else:
	pass


