#!/bin/python3

"""
  Conjunto de datos en python

  * list
  * dict
  * tuple (par)
  * set
"""

# TUPLE: lista inmutable
#
#

tupla = ( 0, 0, 0 )
print(tupla[0])         # se puede acceder 
# tupla[0] = 1          # la tuple no permite modificar su contendio
tupla = ( 1, 0, 0 )


# SET: conjunto
#   * se define por los caracteres {}
#   * no persiste elementos repetidos
#   * a diferencia de los diccionarios no referencia un valor con una clave
#   * a diferencia de los diccionarios no referencia un valor con una clave
#   * es mutable

conjunto = { 1, 2, 3, 4, 6, 7, 8, 9, 9, None }    # "None" es el tipo de dato vacio
print(conjunto)
# print(conjunto[1])      # no es posible acceder a sus elementos

# operaciones 
base = conjunto
referenca = { 3, 7, 9, 10 }

resultado = base & referenca          # interseccion de conjuntos, 
# resultado = base.intersection(referenca)
print("interseccion", base, referenca, resultado)

resultado = base | referenca          # union de conjuntos, .union()
print("union", base, referenca, resultado)
# resultado = base.union(referenca)

resultado = base - referenca          # exclusion de conjuntos
print("diferencia", base, referenca, resultado)

resultado = base ^ referenca          # exclusion simetrica de conjuntos
print("diferencia simetrica", base, referenca, resultado)

base.add('a')
print("base:", base)
base.remove(3);
print("base:", base)
