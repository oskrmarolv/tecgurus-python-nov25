#!/bin/python3

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
