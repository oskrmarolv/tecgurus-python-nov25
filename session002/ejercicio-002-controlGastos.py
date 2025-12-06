#!/bin/python3

"""
	ACCESO A ARCHIVOS

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


print("CONTROL DE GASTOS +++");

while True:
	print("")
	print("Selecciona una opcion:")
	print("\t1) Estado actual de gastos")
	print("\t2) Registrar nuevo gasto")
	print("\t3) Salir")
	option = input(": ");

	if option == "1":
		print(f"{'Categoria':<15} | {'Acumulado':<15}")
		print(f"{'-'*15} | {'-'*15}")
		for category,amount in monthly_expenses.items():
			print(f"{category:<15} | {amount:<15}")
	
	elif option == "2":
		category = input("\tCategoria: ");
		amount = input("tValor del gasto: ");

		unit_expenses.append((category, amount))

		print(unit_expenses)
	
	elif option == "3":
		monthly_expenses, unit_expenses = update_monthly_expenses(monthly_expenses, unit_expenses)

		# SECCION QUE GUARDARA eEL STATUS DE "monthly_expenses" EN UN ARCHIVO

		break;

	else:
		print("OPCION NO VALIDA! Seleccion una opcion del menu.")


print("Hasta la proxima 😎")