#!/bin/python3

"""
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
  print("\t3) Salir")
  option = input(": ");

  print("")

  option = int(option);
  match option:
    case 1:
      task = input("Nueva tarea: ")

      task_list.append(task)

    case 2:
      print("Tareas pendientes")

      for index,task in enumerate(task_list):
        print(f"{index}) {task}")

      print(task_status);

    case 3:
      """
        Agregar un opcion donde permita indicar una tarea completada.
        Se debe eliminar de la lista de tareas y actualizar el 
        diccionario "task_status"
      """
      pass

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
