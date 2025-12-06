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
# print(tupla[0])         # se puede acceder 
# tupla[0] = 1          # la tuple no permite modificar su contendio
tupla = ( 1, 0, 0 )


# SET: conjunto
#   * se define por los caracteres {}
#   * no persiste elementos repetidos
#   * a diferencia de los diccionarios no referencia un valor con una clave
#   * es mutable

conjunto = { 1, 2, 3, 4, 6, 7, 8, 9, 9, None }    # "None" es el tipo de dato vacio
# print(conjunto)
# print(conjunto[1])      # no es posible acceder a sus elementos

# operaciones 
base = conjunto
referenca = { 3, 7, 9, 10 }

resultado = base & referenca          # interseccion de conjuntos, 
# resultado = base.intersection(referenca)
# print("interseccion", base, referenca, resultado)

resultado = base | referenca          # union de conjuntos, .union()
# print("union", base, referenca, resultado)
# resultado = base.union(referenca)

resultado = base - referenca          # exclusion de conjuntos
# print("diferencia", base, referenca, resultado)

resultado = base ^ referenca          # exclusion simetrica de conjuntos
# print("diferencia simetrica", base, referenca, resultado)

base.add('a')
# print("base:", base)
base.remove(3);
# print("base:", base)

# LIST: listas por comprension
lista_enteros = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

# lista_modificada = [ ]
# for numero in lista_enteros:
#   if numero % 2:
#     lista_modificada.append(numero * 2)

# lista por comprension: operan sobre cada elemento aplicando una operacion SENCILLA
# [ operacion iterador condicional ]
lista_modificada = [ numero * 2 for numero in lista_enteros if numero % 2 ]
# print(lista_enteros, lista_modificada)

lista_candena = "ola ke ase... aprendiendo python"
lista_modificada = [ caracter.upper() for caracter in lista_candena ]
# print(lista_candena, lista_modificada)

# slicing
# [ inicio : limite_superior : paso ]
lista_modificada = lista_candena[0:13:2]
# print(lista_candena, " || ", lista_modificada)

lista_modificada = lista_enteros[:5]
# print(lista_enteros, " || ", lista_modificada)


# ERROR MAS COMUN AL TRABAJAR
# CON CONJUNTOS DE DATOS

# La copia de los conjuntos de datos siempre duplica referencia
# y no contenido

print("original:", lista_enteros)

lista_enteros[1] = "cadena"
lista_enteros[5] = [ 'a', 'e', 'i', 'o', 'u' ]
print("modificacion:", lista_enteros)

# realizando copia "clasica"
# lista_copiada = lista_enteros
# realizando copia real
lista_copiada = lista_enteros[:]            # copia literal mas no profunda...
lista_copiada[5] = None
# lista_copiada[5][1] = None
print("listas_enteros:", lista_enteros)
print("listas_copiada:", lista_copiada)


