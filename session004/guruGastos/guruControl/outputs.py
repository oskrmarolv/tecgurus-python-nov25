#!/bin/python3

def output_monthly_expenses(expense_status, currency = 1):
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

def output_menu_app():
	"""
		Salida en consola de menu

		None output_menu_app()
	"""
	print("")
	print("Selecciona una opcion:")
	print("\t1) Balance actual de gastos")
	print("\t2) Registrar nuevo gasto")
	print("\t3) Actualizar balance")
	print("\t4) Salir")

def output_goodbye():
	pass

def output_country ():
	print("Moneda: Mexico")
