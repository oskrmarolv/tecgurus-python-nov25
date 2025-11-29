#!/bin/python3

"""
  FUNCIONES



  Ejercicio: El Organizador de Tareas (Listas y Bucles while)
  
  Este ejercicio te ayudará a entender cómo manipular listas dinámicamente y cómo controlar el flujo del programa con un menú interactivo.

  El Reto: Crea un programa que actúe como una lista de tareas "To-Do".

  El programa debe iniciar con una lista vacía.

  Debe mostrar un menú infinito (while True) con 3 opciones:

  1: Agregar tarea.

  2: Ver tareas pendientes.

  3: Salir.

  Si el usuario elige "1", pide el nombre de la tarea y agrégala a la lista.

  Si elige "2", muestra todas las tareas usando un bucle for (imprime el número de tarea también).

  Si elige "3", rompe el ciclo (break) y despídete.

"""



# FUNCIONES
#     * uso de "snake_case"
#     * siempre definir su Docstring
#
#     def NOMBRE_DE_LA_FUNCION ( ARGUMENTOS... ):
#       pass
#
#

#def funcion_generica(texto, numero):        # argumentos por diccionario
#def funcion_generica(texto="", numero):     # argumentos con valor por defecto
# def funcion_generica(texto, numero):        
#  return          # retorna siempre "None"


# Funcion pura / funcion propia (trabaja solo con variables dentro de la funcion)
# argumento con valor por defecto
def new_task(l, n="Generico"):
  """
    Captura un elemento y agrega a una lista

    list new_task(list l, string n="Generico")
  """
  new_list = l[:]

  task = input(f"{n} agrega una nueva tarea: ")
  new_list.append(task)
  return new_list

# Funcion impura / funcion impropia (accede a variables fuera de la funcion)
# OJO!!  el valor por defecto de "temporal" crea una sola instancia
#         de la lista y no una lista por cada llamada a la funcion
def list_task (l, arg_trampa=[ 0 ]):
  """
    Salida en consola de la lista de tareas

    None list_task(list l)
  """
  print("+ Tareas pendientes")

  temporal_list = l[:]
  for index,task in enumerate(temporal_list):
    print(f"{index}) {task}")

  #arg_trampa.append(task);
  t = arg_trampa[:]
  t.append(task);

  print(task_status, t);

# Argumentos variables (*arg, **kwargs)
# def complete_task (l, i_task1, i_task2=None, i_task3=None):
#
#     *args          define tupla de longitud "n"
#     **kwargs       define un diccionario de claves "n"
def complete_task (l, **tareas):
  print(l, type(l))
  print(tareas, type(tareas))

  return l




# -------------------------------------------
# main --------------------------------------
# -------------------------------------------

task_list = [ "Subir material a la plataforma", "Subir ejemplos al repositorio", "Preparar presentacion" ]

task_status = {
  "success": 0,
  "pending": 0, 
  "skipped": 0
}


print("")
print("+++ APLICACION DE TAREAS +++\n")
print("")

flag_control = True
# while True:                         # requiere sentencia 'break'
while flag_control:
  task_status["pending"] = len(task_list)

  print("")
  print("Selecciona una opcion:")
  print("\t1) Agregar nueva tarea")
  print("\t2) Listar tareas")
  print("\t3) Completar tareas")
  print("\t4) Salir")
  option = input(": ");

  print("")

  option = int(option);
  match option:
    case 1:
      #task_list = new_task(task_list)       # argumentos por enumeracion
      #task_list = new_task(l=task_list)     # argumentos por diccionario
      task_list = new_task(n="Oscar", l=task_list)     # argumentos por diccionario

    case 2:
      list_task(task_list)
      #print(temporal)

    case 3:
      """
        Agregar un opcion donde permita indicar tareas completadas.
        Se deben eliminar de la lista de tareas y actualizar el 
        diccionario "task_status"
      """
      task_list = complete_task(task_list, 1, 2, 7)
      #task_list = complete_task(task_list, x=1, y=2, z=7)

    case 4:
      flag_control = False
      break                         # si la definicion fue con "while True:"
      pass

    case _:
      print("OPCION NO VALIDA! Por favor ingresa una opcion correcta.")


# las estructuras de control no generan un ambito propio 
# en la definicion de variables (usan el ambito del flujo 
# principal)
# print("scopes:", task, option)
print("++ ADIOS!!")
