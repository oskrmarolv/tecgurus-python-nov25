#!/bin/python3

"""
Python desde cero - Nov2025

TEMAS
* Variables
* Tipos de datos primitivos
* Operadores
"""


"""
Tipo de datos primitivos

PEP: Definicion de variables
  * definicion de nombres con minuscula
    entero  ✅
    Entero  ❌
    ENTERO  ❌
  * uso de notacion "Snake case"
    entero_uno  ✅
    entero_Uno  ❌
    enteroUno   ❌
  * nombres de variables altamente descriptivas (pref. en ingles)
    control_integer   ✅
    entero_de_control ✅
    entero_uno        ❌
  * no definir palabras reservadas
    class_human ✅
    class       ❌
    for         ❌
    while       ❌
    def         ❌
    pass        ❌

"""
entero = 1                  # numero entero
complejo = 3 + 7j           # numero complejo
decimal = 3.14              # numero decimal
caracter = 'c'              # caracter de texto
cadena = "Cadena de texto"  # cadena de texto
booleano = True             # True, False


"""
Operadores

PEP:
  * los operadores siempre deben ir acompañados de espacios
"""

x = 1
y = 2

# aritmeticos
z = x + y     # suma
z = x - y     # resta
z = x * y     # multiplicacion
z = x / 2     # divicion
z = x ** y    # potencia
z = x % y     # modulo (residuo en la division)

# comparacion

es_igual = ( x == y )           #
es_mayor = ( x > y )            #
es_meno_igual = ( x <= y )      #
es_diferente = ( x != y )       #

# logicos

alterego = False

operador_and = booleano and alterego
operador_or = booleano or alterego
operador_not = not alterego


"""
  print()

  salida en consola comoda
"""

print(entero)       # directa
print("imaginario", complejo, complejo.real, complejo.imag)     # varios valores
print(f"Valor de PI: {decimal}")      #f-string
# print("Valor de PI: %" % decimal)        # deprecated!!
print(caracter, "a", "r", "a", "c", "t", "e", "r", sep="|")
print(cadena)
print(booleano)


"""
  input()

  recibie un dato de entrada desde teclado
"""

dato = input("ingresa dato: ")
print(dato, type(dato))

dato = int(dato)      # float() bool() str()
print(dato, type(dato))

print(oef)