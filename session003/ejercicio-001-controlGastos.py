#!/bin/python3

"""
	+ MANEJO DE EXCEPCIONES

	ACCESO A ARCHIVOS

	INTRODUCCION A MODULOS
"""


# INTRODUCCION AL MANEJO DE MODULOS
# 
# 	Agregando definiciones para su implementacion en el proyecto
#		import NOMBRE_PAQUETE
# 		from NOMBRE_PAQUETE import DEFINICION, DEFINICION, DEFINICION, ...
# 		from NOMBRE_PAQUETE import DEFINICION as REFERENCIA, DEFINICION as REFERENCIA, DEFINICION as REFERENCIA, ...

import math 			# definiciones de la biblioteca "math" de python-core
import random			# definiciones de la biblioteca "random" de python-core
from datetime import datetime
# from datetime import datetime as timestamp



def output_monthly_expenses(expense_status):
	"""
		Salida en consola de gastos

		None output_monthly_expenses(dict expense_status)
	"""
	print("")
	print(f"\t{'CATEGORIA':<15} | {'ACUMULADO':<15}")
	print(f"\t{'-'*15} | {'-'*15}")
	for category,amount in expense_status.items():
		print(f"\t{category:<15} | {amount} ({amount * currency} MX)")
	print("")	

def update_monthly_expenses(unit, expense_status):
	"""
		Actualizacion de balance por categoria

		tuple update_monthly_expenses(list unit, dict expense_status)
	"""
	# creando diccionario por comprension
	update_status = { category:amount for category,amount in expense_status.items() }

	# recorriendo montos unitarios
	for category,amount in unit:
		# ERROR: no puedo asegurar que "category" existe
		# update_status[category] = update_status[category] + amount

		if category not in update_status.keys():
			update_status[category] = 0.0

		update_status[category] += amount
		
	return update_status, [ ]


# -----------------------------------
# main ------------------------------
# -----------------------------------

# SECCION DONDE RECUPERAMOS EL ULTIMO ESTADO DE "monthly_expenses"

access_timestamp = datetime.now()

monthly_expenses = None
# monthly_expenses = { 
# 	"comida": 0.0,
# 	"transporte": 0.0,
# 	"recreacion": 0.0,
# 	"suscripciones": 0.0
# }

# MANEJO DE ARCHIVOS
# 
# Acceso a archivos
#		* Creacion de archivos con notacion "snake_case"
#		* La ruta del archivo se sugiere relativa
#
# open(file, mode, encoding, newline)
#  mode: r (read), (w writte), (a append)

# Metodo modero (> 3.x.x)
# 	use de with (Manejador de contexto)

with open("balance_file.txt", 'r', encoding="utf-8") as last_balance_file:
	data = last_balance_file.read()
	monthly_expenses = eval(data)

unit_expenses = [ ]

# currency = 0
currency = 19.35

print("CONTROL DE GASTOS + + +");
print("(MX) -> (US)");
print("")
print(f"Balance actual ({ access_timestamp.strftime("%Y/%m/%d %H:%M") }) =>")
output_monthly_expenses(monthly_expenses)


flow_ctrl = True
while flow_ctrl:
	print("")
	print("Selecciona una opcion:")
	print("\t1) Balance actual de gastos")
	print("\t2) Registrar nuevo gasto")
	print("\t3) Actualizar balance")
	print("\t4) Salir")
	option = input(": ");

	if option == "1":
		output_monthly_expenses(monthly_expenses)
	
	elif option == "2":
		print("")
		category = input("+ Categoria: ")
		amount = input("+ Cantidad: ")

		# amount = float(amount)

		# MANEJO DE EXCEPCIONES EN PYTHON
		# 	try - catch - finally 					otros lenguajes
		# 	try - except - else - finally			en Python

		try: 
			# Bloque principal que buscar contener
			# operaciones o flujos muy puntuales

			# Operacion con posible error:
			# 	el cast a un numero flotante no
			# 	convierte cualquier string
			amount = float(amount)

			if amount == 0.0:
				raise Exception("El monto no puede ser cero.", 100)
			else:
				amount = amount / currency

		except ValueError as value:
			print("")
			print(f"Monto invalido: {value}!\nNo es posible registrar el monto para la categoria {category}.")
			print("")

		except ZeroDivisionError:
			print("")
			print(f"La conversion a moneda no es valida!\nNo es posible registrar el monto para la categoria {category}.")
			print("")

		# except:
			# NO SE RECOMIENDA: al ser un camino que me permite
			# recuperar cualquier tipo de error se requeriria
			# dar un tratamiento explicito a todo.

		except Exception as error:
			# BaseException: error generico que captura casos no contemplados
			# 	"as" crea una referencia a un objeto principal

			print("")
			# print(f"Operacion no valida!\n Causa: {error}")

			# ERROR: __str__() se incoca y no tiene una representacion de ese tipo
			# print(f"Operacion no valida!\n Causa: {error[0]} (codigo: {error[1]})")
			print(f"Operacion no valida!\nCausa: {error.args[0]} (codigo x{error.args[1]})")
			print("")

		else:
			# Bloque que solo se ejecuta si el bloque
			# principal (try) no detona error alguno

			# Se suele utilizar cuando se require 
			# ejecutar operaciones secundarios

			unit_expenses.append((category, amount))

		finally:
			# Bloque que siempre se ejecuta sin importar
			# si existio error o no

			# Se suele utilizar para asegurar que algunas 
			# operaciones se ejecutaran 

			print(f"+ Gastos unitarios en sesion:")
			print(f"  {unit_expenses}" )

	elif option == "3":
		monthly_expenses, unit_expenses = update_monthly_expenses(unit_expenses, monthly_expenses)

		output_monthly_expenses(monthly_expenses)

	elif option == "4":
		# MANEJO DE ARCHIVOS
		
		# Metodo clasico (< 3.x.x)
		# 	definicion de "fd" es completamente responsabilidad
		#	del desarrollador (open(), close())
	
		try: 
			# esto puede fallar y corromper el archivo si 
			# no se cierra de manera adecuada
			balance_file = open("balance_file.txt", "w", encoding="utf-8")
			balance_file.write(str(monthly_expenses))

		except OSError as err:
			print(f"ERROR :: Fallo durante el proceso de escritura: {err}")

			# EJERCICIO: Pedir confirmacion para salir de la ejecucion
			# 	Estas seguro de salir ?  Se perdera los cambios. (s/n) 
		
		else: 
			flow_ctrl = False

		finally:
			balance_file.close()

	else:
		print("OPCION NO VALIDA! Seleccion una opcion del menu.")
		
print("Hasta luego 🤓!")