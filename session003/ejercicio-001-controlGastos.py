#!/bin/python3

"""
	MANEJO DE EXCEPCIONES

	ACCESO A ARCHIVOS

	INTRODUCCION A MODULOS
"""



def update_monthly_expenses(expense_status, unit):
	update_status = { }

	return update_status, [ ]
	pass


# -----------------------------------
# main ------------------------------
# -----------------------------------

# SECCION DONDE RECUPERAMOS EL ULTIMO ESTADO DE "monthly_expenses"
monthly_expenses = { 
	"comida": 0.0,
	"transporte": 0.0,
	"recreacion": 0.0,
	"suscripciones": 0.0
}
unit_expenses = [ ]

# currency = 0
currency = 19.35


print("CONTROL DE GASTOS + + +");
print("(MX) -> (US)");

while True:
	print("")
	print("Selecciona una opcion:")
	print("\t1) Balance actual de gastos")
	print("\t2) Registrar nuevo gasto")
	print("\t3) Actualizar balance")
	print("\t4) Salir")
	option = input(": ");

	if option == "1":
		print("")
		print(f"\t{'CATEGORIA':<15} | {'ACUMULADO':<15}")
		print(f"\t{'-'*15} | {'-'*15}")
		for category,amount in monthly_expenses.items():
			print(f"\t{category:<15} | {amount} ({amount * currency} MX)")
		print("")
	
	elif option == "2":
		print("")
		category = input("+ Categoria: ")
		amount = input("+ Cantidad: ")

		# amount = float(amount)

		# MANEJO DE EXCEPCIONES EN PYTHON
		# try - catch - finally 				otros lenguajes
		# try - except - else - finally			en Python

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
		pass

	elif option == "4":

		# SECCION QUE GUARDARA EL STATUS DE "monthly_expenses" EN UN ARCHIVO

		break;

	else:
		print("OPCION NO VALIDA! Seleccion una opcion del menu.")


print("Hasta la proxima 😎")