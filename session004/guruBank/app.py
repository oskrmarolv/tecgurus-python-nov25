#!/bin/python3

"""
  PROGRAMACION ORIENTADA A OBJETOS (POO)
  EN PYTHON

  La POO es un paradigma en la programacion que busca simular la realidad (REALIDAD: es el entorno donde el ente tienen sentido) al abstraerla en terminos simples
  
  Algunos tipos de paradigmas en la programacion
	- Estructurada
	- Orientada a objetos ***
	- Orientado a eventos
	- Funcional


  > Pilars de la POO

	* Abstraccion
	* Encapsulamiento
	* Herencia
	* Polimorfismo


  > Conceptos fundamentales

	CLASE: Plantalla o Estructura base que me permite definir en terminos simples ente dentro de una realidad
	  - Atributos: valores
	  - Metodos: acciones

	OBJETO: La creacion de un ENTE a partir de la definicion de una clase que asigna valores concretos a 
			los atributos y/o metodos (INSTANCIAR un objeto)
"""

"""
	GURU-BANK:

	  Ejercicio que simule el funcionamiento de un banco (GURU-BANK)
		- El banco debe existir
		- El bacno administra cuentas que los usuarios pueden abrir
		- Los usuarios guardan sus ingresos en esas cuentas
		- Los usuarios tiene la posibilidad de operar con su dinero
			- Para transferencias: cuenta es DEBITO el saldo aumento
			- Para transferencias: cuenta es CREDITO el saldo disminuye
"""

# REALIDAD: sistema bancario

# POO: ABSTRACCION
#   Es la definicion de las caracteristicas
#   primordiales que hace que un ente 
#   pueda exisitir dentro de una realidad

# Definicion de CLASE
#     * Definicion con la notacion "CameleCase"
#
#	class NombreClase:
#		pass
#
class User:
	"""
	Define las propiedades, caracteristicas que hacen unico a un usuario
	"""

	# Metodo Constructor: es el punto de entrada que me permtira instanciar un objeto 
	# dentro de esa realidad. Es el primer metodo que se invoca cuando se crea un objeto
	#
	# 	self: hace referencia a "MI MISMO". Es el equivalente a "this" en 
	#		otros lenguajes de programacion y debe ser enviado siempre como 
	#		primer argumento dentro de los metodos
	def __init__(self, name, age, ine_id):
		# Atributos (de instancia)
		self.name = name
		self.age = age
		self.ine_id = ine_id

	# Metodo (de instancia)
	def hello(self):
		return f"Hello! My name is {self.name} 😎"

	def show_ine_id(self):
		return self.ine_id

	# __str__()
	# Equivalente a object.toString() en otros lenguajes de programacion
	def __str__(self):
		return f"{self.name} (id: {self.ine_id})"

# POO: Encapsulamiento
# 	Permite marcar un limite en como se define la
#		clase y como interactual con elementos externos
#
#		No existe el concepto de "Modificadores de acceso"
#		como en otros lenguajes de programacion
#			- public 			todo es publico 
#			- protected		no existe. solo es "MORAL"
#			- private 		se simula
class Account:
	"""
	Define las propiedades, caracteristicas que hacen unico a una cuenta de banco
	"""

	# Atributo (de clase): similar al modificador de acceso "protected"
	#						en otros lenguajes de programacion porque estaria
	#						directamente asociado a una clase (no a una instancia)
	# seq_account_id = 1000
	__seq_account_id = 1000

	def __init__(self, type):
		# atributo de instancia tipo "private"
		#	python crear un arbol del tipo => self.__Account__.__id
		# self.__id = Account.seq_account_id
		self.__id = Account.__seq_account_id

		# atributo de instancia tipo "protected"
		# 	python lo ve como un atributor publico pero
		#		se le indica al desarrollador que sea tratado
		#		como "protected"
		self._status = "active"

		# atributo de instancia tipo "public"
		self.type = type		# credit | debit

		# atributo de clase
		Account.__seq_account_id += 1

	# SETTER / GETTER
	#
	# DECORADORES: etiquetas que indican al intrerprete  de python
	# que la definicion debe tener un comportamiento especifico
	#		@property
	#		@ALIAS_NAME.setter
	@property
	def identification(self):
		return self.__id

	# NOTA: NO TIENE SENTIDO DEFINIR TANTO SETTER + GETTER
	# PARA UN MISMO ATRIBUTO PRIVADO
	@identification.setter
	# def identification(self, new_id):
	# 	if new_id > 0:
	# 		self.__id = new_id
	# 	else:
	# 		print("El valor de ID no es valido")

# POO: Herencia
# 	Mecanismo a travez del cual una clase (sub-clase 
#		o clase-hija) retoma definiciones desde otra 
#		clase superior (super-clase o clase-padre)
#		
#	* No hereda nada que sea "private"
#	* Si existe la multi-herencia y es resuelta mediante "MRO" (Module Resolution Order)
#			
#
#	class NombreClase(NombreClasePadreA, NombreClasePadreB, ...):
#		pass
#	
# PROBLEMA DEL DIAMANTE (consecuencia de la multi-herencia)
#	MRO: local -> NombreClasePadreA -> NombreClasePadreB -> ...
#			el proceso termina en el primer instante 
#			que encuentra una coincidencia
class AccountBank(Account):
	"""docstring for AccountBank"""
	def __init__(self, user: User, type_account: str, initial_balance: float = 0.0):
		self.user = user
		self.__balance = initial_balance

		# super()  accede a la definicion de la clase-padre para instanciar
		# 		Account.__init__(*args)
		super().__init__(type_account)

	@property
	def balance(self):
		return self.__balance
	
	def deposit(self, amount: float):
		if self.type == "credit":
			self.__balance -= amount
		elif self.type == "debit":
			self.__balance += amount
		else:
			print("Tipo de cuenta no identificada")



class Bank:
	pass


print("")
print("")
# ----------------------------------------------
# MAIN -----------------------------------------
# ----------------------------------------------

if __name__ == "__main__":

	# INSTANCIANDO un objeto
	#		A diferencia de otros lenguajes de programacion
	#		no existe la palabra reservada "new" en el
	#		proceso de instancia
	#
	# Invocando el metodo __init__() de la clase
	# 	_.__create__(User) 					-> self
	# 	User.__init__(self, **kwargs)		-> object
	usuario_oscar = User("Oscar", "30", "2378458723-465")
	print("Usuario:", usuario_oscar)
	print(f"Identificador: {usuario_oscar.show_ine_id()}")
	# usuario_oscar.hello()

	# usuario_oscar.name = "Fulanito"			# tal ves esto no sea muy critico...
	# usuario_oscar.hello()

	# account_oscar = Account()
	# account_oscar.__id = 5001				# esto es imposible en el contexto de modificar el atributo privado
	# 										# realmente se se esta creando un atributo nuevo __id

	# account_fulanito = Account()
	# print(f"status: {account_fulanito._status}")
	# print(f"el ID-ORIGINAL es: {account_fulanito.identification}")
	# # SI EL GETTER estuviese definido...
	# # account_fulanito.identification = -3000
	# # print(f"el ID-MODIFICADO es: {account_fulanito.identification}")

	#
	# RETOMANDO AL USUARIO "oscar"
	# 
	print("")

	account_bank_oscar = AccountBank(usuario_oscar, "debit", 100.0)
	print("Estado de la cuenta:", account_bank_oscar._status)
	print("ID de la cuenta:", account_bank_oscar.identification)
	print("Usuario:", account_bank_oscar.user.hello())
	print("Usuario:", account_bank_oscar.user)
	print("Saldo inicial", account_bank_oscar.balance)
	account_bank_oscar.deposit(50.0)
	print("Saldo actual", account_bank_oscar.balance)

# ----------------------------------------------
# end -----------------------------------------
# ----------------------------------------------
print("")
print("")
