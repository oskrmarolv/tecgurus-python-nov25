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
			- Para transferencias: cuentas de CREDITO no pueden transferir
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
		self.key = "tecgurus"

	# Metodo (de instancia)
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

	# Atributo (de clase)
	# seq_account_id = 1000
	__seq_account_id = 10000000

	def __init__(self, user, type_account):
		# atributo de instancia tipo "private"
		self.__id = Account.__seq_account_id

		# atributo de instancia tipo "protected"
		self._status = "active"

		# atributo de instancia tipo "public"
		self.owner = user
		self.type = type_account
		self.note = "Cuenta de bancop generica"

		# atributo de clase
		Account.__seq_account_id += 1

	# SETTER / GETTER
	@property
	def id(self):
		return self.__id

	def deposit(self):
		return None

	def retreat(self):
		return None

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
#		MRO: local 	-> 	NombreClasePadreA 	-> 	NombreClasePadreB 	-> 	...
#
#		el proceso termina en el primer instante 
#		que encuentra una coincidencia
class DebitAccount(Account):
	"""
	Clase que define una cuenta de tipo "debit"
	"""

	TYPE = "debit"

	def __init__(self, user: User, initial_balance: float = 0.0):
		self.__balance = initial_balance

		# super() 
		# Accede a la definicion de la clase-padre para instanciar
		# 		Account.__init__(*args)
		super().__init__(user, DebitAccount.TYPE)

	@property
	def balance(self):
		return self.__balance

	# Sobreescritura de metodos
	#		solo puede darse en metodos de instancia
	def deposit(self, amount):
		if amount > 0.0:
			self.__balance += amount
			return True
		else:
			return False

	def retreat(self, amount):
		if amount > 0.0 and self.__balance >= amount:
			self.__balance -= amount
			return amount
		else: 
			return None

# POO: Polimorfismo
# 	Proceso mediante el cual, a traves de la herencia,
# 	clases similares realizan acciones de manera distintas
#
#  	Crea la base para el concepto de "especializacion"
#		La defincion de clases que modifican su comporamiento
# 	a un punto muy especifico
#
#		sobreescritura de metodos: que sobreescribe el comportamiento
#					de un metodo para hacerlo propio en una clase
#
#		En Python no existe la sobrecarga de metodos (*args, **kwargs)
class CreditAccount(Account):
	"""
	Clase que define una cuenta de tipo "credit"
	"""
	TYPE = "credit"

	def __init__(self, user):
		self.__balance = 5000.0

		# super()
		# Accede a la definicion de la clase-padre para instanciar
		# 		Account.__init__(*args)
		super().__init__(user, CreditAccount.TYPE)

	@property
	def balance(self):
		return self.__balance

	# Sobreescritura de metodos
	#		solo puede darse en metodos de instancia
	def deposit(self, amount): 
		if amount > 0.0:
			self.__balance -= amount
			return True
		else: 
			return False

# PROPUESTA 
# Busca generar una realidad mucho mas dinamica
class SystemBank: 
	
	def __init__(self, user):
		self.user = user
		self.__accounts = { }
		self.__confidential = {
			key: "tecgurus"
		}

	def create_account(self, type_account, amount = 0.0):
		pass

	def is_authorized(self, key):
		pass

class GuruBank:
	
	def __init__(self):
		self.name = "GURU-BAN"
		# { account_id: (user, account) }
		self.__accounts = { }

	def get_account_list(self):
		print("")
		print(f"----- {self.name}: Account's -----")
		print("")

		if not self.__accounts:
			print("\twithout accounts...")

		print(f"{"#":<10} | {"Owner":<10} | {"Type":<10} | Balance (current)")
		print(f"{"-"*10} | {"-"*10} | {"-"*10} | {"-"*10}")
		for id, row in self.__accounts.items():
			user, account = row
			print(f"{id:<10} | {user.name:<10} | {account.type:<10} | {account.balance:<10}")

	def get_accounts_by_user_id(self, ine_to_search):
		accounts = [ ]

		for account_id, row in self.__accounts.items():
				user, account = row

				if ine_to_search == user.ine_id:
					accounts.append(account_id)

		return accounts

	def create_account(self, user, type_account, amount = 0.0):
		account = None
		match type_account:
			case "debit":
				account = DebitAccount(user, amount)

			case "credit":
				account = CreditAccount(user)

			case _:
				return False

		self.__accounts[account.id] = (user, account)
		return True

	def transaction_account_transfer(self, orig, dest, amount_to_tranfer):
		if not orig in self.__accounts or not dest in self.__accounts:
			return

		user_orig, account_orig = self.__accounts[orig]
		user_dest, account_dest = self.__accounts[dest]

		if account_orig.type == "credit":
			return False

		amount = account_orig.retreat(amount_to_tranfer) 
		if amount:
			return account_dest.deposit(amount)
		else:
			return False

	def transaction_account_deposit(self, account, amount, user_key):
		pass

	def transaction_retreat(self, account, amount, user_key):
		pass

print("")
print("")
# ----------------------------------------------
# MAIN -----------------------------------------
# ----------------------------------------------

if __name__ == "__main__":
	gurubank = GuruBank()

	# Invocando el metodo __init__() de la clase
	# 	_.__create__(User) 								-> self
	# 	User.__init__(self, **kwargs)			-> object
	usuario_oscar = User("Oscar", "30", "2378458723-465")
	usuario_gabriel = User("Gabriel", "28", "2378458723-462")
	usuario_jonathan = User("Jonathan", "20", "2378458723-466")
	usuario_maya = User("Maya", "27", "2378458723-469")

	gurubank.create_account(usuario_oscar, "debit", 100.0)
	gurubank.create_account(usuario_gabriel, "credit")
	gurubank.create_account(usuario_jonathan, "afore", 100.0)
	gurubank.create_account(usuario_maya, "debit", 500.0)
	gurubank.create_account(usuario_oscar, "credit")

	print("")
	print("Estado inicial...")
	gurubank.get_account_list()

	# transacciones...
	accounts_oscar = gurubank.get_accounts_by_user_id(usuario_oscar.ine_id)
	accounts_gabriel = gurubank.get_accounts_by_user_id(usuario_gabriel.ine_id)

	account_orig = accounts_oscar[0]
	account_dest = accounts_gabriel[0]
	gurubank.transaction_account_transfer(account_orig, account_dest, 100.0)

	print("")
	print("Al finalizar operaciones...")
	gurubank.get_account_list()


# ----------------------------------------------
# end -----------------------------------------
# ----------------------------------------------
print("")
print("")