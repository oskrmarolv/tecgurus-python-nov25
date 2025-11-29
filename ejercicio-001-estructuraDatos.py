#!/bin/python3

"""
  TEMA: Estructuras de datos (list, dicc, tuple, par)
"""

"""
  Creacion de un blog de tareas
"""

# LISTA

task_list = [ "Generar presentacion", "Conectar pantalla main, reviewer" ]
print(task_list)

# acceso a los elementos a traves de un indice
#     - el indice siempre comienza en "0"
print(task_list[1])
#print(task_list[2])

task_list[0] = "Generar presentacion en formato PDF";

# el rando de indices siempre corresponde a len(..)-1
print(len(task_list))

# append(): agregar elemento al final de la lista
task_list.append("Subir material del curso a la plataforma")
task_list.append("Crear repositorio del curso")
task_list.append("Agregar comentarios a codigos")

# insert(): insertar elemento en un indice especifico
task_list.insert(2, "Pasar asistencia")
print("lista despues de insert() ==>", task_list, "\n")

# pop(): saca un elemento de la lista
task = task_list.pop(3)
print("lista despues de pop() ==>", task_list, "tarea actual", task, "\n")

# sort(): ordena la lista
task_list.sort()
print("lista despues de pop() ==>", task_list)


# DICCIONARIO

status_task = {
  "success": 0,
  "pending": 0,
  "skipped": 0
}

print(f"task success = {status_task["success"]}")

status_task["success"] += 1;
print(status_task)

# keys(): retorna lista de claves
print(status_task.keys())

# values(): retorna lista de valores
print(status_task.values())

# items(): retorna lista de tuplas con pares ordenados
#     ** la tupla es un caso especial de la lista con la caracteristica de ser inmutable, se define con () **
print(status_task.items())

for clave,valor in status_task.items():
  print(f"{clave} -> {valor}")
