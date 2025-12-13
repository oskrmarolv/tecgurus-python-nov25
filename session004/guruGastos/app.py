#!/bin/python3

"""
	INTRODUCCION A MODULOS
"""

# INTRODUCCION AL MANEJO DE MODULOS
# 
# 	Agregando definiciones para su implementacion en el proyecto
#			import NOMBRE_PAQUETE
# 		from NOMBRE_PAQUETE import DEFINICION, DEFINICION, DEFINICION, ...
# 		from NOMBRE_PAQUETE import DEFINICION as REFERENCIA, ...

import math 			# definiciones de la biblioteca "math" de python-core
import random			# definiciones de la biblioteca "random" de python-core
from datetime import datetime
# from datetime import datetime as timestamp

# ERROR!! import "./control/outputs" 
# 1ra forma: import control.outputs; 
# 2da forma: from control import outputs as o, actions

from guruControl import output_monthly_expenses, output_menu_app, output_country, update_monthly_expenses, CURRENCY, COUNTRY


# VALORES INICIALES...

access_timestamp = datetime.now()

unit_expenses = [ ]

monthly_expenses = None
with open("balance_file.txt", 'r', encoding="utf-8") as last_balance_file:
	data = last_balance_file.read()
	monthly_expenses = eval(data)


# -----------------------------------
# main ------------------------------
# -----------------------------------

# Equivalente de "void function main( ) { ... }" en C
# Equivalente de "static void main( ) { ... }" en Java

if __name__ == "__main__":

	print("CONTROL DE GASTOS + + +");
	print("(MX) -> (US)");
	print("")
	print(f"Balance actual ({ access_timestamp.strftime("%Y/%m/%d %H:%M") }) =>")
	# 1ra forma: control.outputs.output_monthly_expenses(monthly_expenses, CURRENCY)
	# 2da forma: o.output_monthly_expenses(monthly_expenses, const.CURRENCY)
	output_monthly_expenses(monthly_expenses, CURRENCY)

	flow_ctrl = True
	while flow_ctrl:
		
		## MENU
		output_menu_app()

		option = input(": ");

		if option == "1":
			output_monthly_expenses(monthly_expenses, CURRENCY)
		
		elif option == "2":
			print("")
			category = input("+ Categoria: ")
			amount = input("+ Cantidad: ")

			try: 
				amount = float(amount)

				if amount == 0.0:
					raise Exception("El monto no puede ser cero.", 100)
				else:
					amount = amount / CURRENCY

			except ValueError as value:
				print("")
				print(f"Monto invalido: {value}!\nNo es posible registrar el monto para la categoria {category}.")
				print("")

			except ZeroDivisionError:
				print("")
				print(f"La conversion a moneda no es valida!\nNo es posible registrar el monto para la categoria {category}.")
				print("")

			except Exception as error:

				print("")
				print(f"Operacion no valida!\nCausa: {error.args[0]} (codigo x{error.args[1]})")
				print("")

			else:

				unit_expenses.append((category, amount))

			finally:
				
				print(f"+ Gastos unitarios en sesion:")
				print(f"  {unit_expenses}" )

		elif option == "3":
			monthly_expenses, unit_expenses = actions.update_monthly_expenses(unit_expenses, monthly_expenses)

			output_monthly_expenses(monthly_expenses, CURRENCY)

		elif option == "4":
			try: 
				balance_file = open("balance_file.txt", "w", encoding="utf-8")
				balance_file.write(str(monthly_expenses))

			except OSError as err:
				print(f"ERROR :: Fallo durante el proceso de escritura: {err}")

			else: 
				flow_ctrl = False

			finally:
				balance_file.close()

		else:
			print("OPCION NO VALIDA! Seleccion una opcion del menu.")
			
	print("Hasta luego 🤓!")