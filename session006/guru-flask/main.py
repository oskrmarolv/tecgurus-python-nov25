#!/bin/python3

# APIRest (JSON)
#  Comunicacion a travez de HTTP
#       metodos (verbos): GET, POST, PUT, DELETE
#       codigo de estado: 100, 200, 300, 400, 500
#
# Otros tipos de comunicaciones:
#   - SOAP (XML)
#   - Websocket (socket.io)
#   - GraphQL (http)

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)       # instancia principal de la aplicacion


# Conexion a base de datos con SQLAlchemy...
# URI: 
# 	protocolo :// user:pass@host:port / resources ? query
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://guru_test:guru_test@127.0.0.1:3306/guru_api"

db = SQLAlchemy(app)

# ORM de Users
class UserOrm(db.Model):
	# atributos de clase -> definicion de tabla en SQL
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(128), nullable = False)
	age = db.Column(db.Integer, nullable = True)

	# metodos de clase
	def to_dict(self):
		return { "id":self.id, "name":self.name }

# creacion de recursos iniciales en la DB
with app.app_context():
	db.create_all()


# definicion de rutas...

@app.get("/")           # MVC: HTTP (method + endpoint)
def init():             # MVC: controlador
 	# response: paylod, http_status_code
 	return "Success", 200

@app.get("/home")
def home():
	# render_template(template, **kwargs_data_bulding) 
 	return render_template("index.html", date_now = "27-dic-2025"), 200


# 
#	API's
# 	Buenas practicas:
# 		- Desarrollo sobre el protocolo HTTP
#		- Construccion de endpoints: define las URL's del servicio API
# 			* Modelo basa en recursos (resource): elemento que contiene operaciones internar. 
#				Se definen en plural e indican elemento unitarios
#			* NO DEFINIR acciones en la estructura de URL, para ello se implementa a traves de los metodos HTTP
#					GET: /users/update    	incorrecto
#					PUT: /users    			CORRECTO !!
#
# 	Estructura de URL
#	protocolo :// direccion_servidor / recurso / sub_recurso ? query

# Concept de CRUD: operaciones basicas
# C - R - U - D

@app.post("/users")
def create_users():
	payload = request.get_json(silent=True) # null -> None, permite omitir posibles errores en el cast de valores JSON a Python
	# { name:null } -> silent=True { }
	# 							-> silent=False ERROR!!
	print("data_request", type(payload), payload)

	new_user = UserOrm(name = payload["name"], age = payload.get("age"))

	# db.session
	# stack con las transacciones pendientes a la DB

	# db.session.add(): agrega un elemento al stack de transacciones
	db.session.add(new_user)			# transformar a SQL el estado actual de la instancia

	# db.session.commit(): se dispara una solicitud de escritura a la DB
	db.session.commit()					# ejecuta el stack actual de sentencias SQL en la DB

	response_data = {
		"status": {
			"code": 0,
			"desc": "Success"
		},
		"data": new_user.to_dict()
	}
	return jsonify(response_data), 201

@app.get("/users")
def read_users():
	users = UserOrm.query.order_by(UserOrm.name.asc()).all()

	# Objeto respuesta
	response_data = {
		# cual es el status del proceso interno
		"status": {
			"code": "0",
			"desc": "Success"
		},
		# payload interno del proceso
		"data": [ user.to_dict() for user in users ]
	}
	return jsonify(response_data), 200

@app.put("/users")
def update_users():
	payload = request.get_json(silent = True)
	user_id = payload["id"]
	update_name = payload["name"]

	user_to_update = db.session.get(UserOrm, user_id)
	user_to_update.name = update_name
	db.session.add(user_to_update)
	db.session.commit()

	response_data = {
		"status": {
			"code": 0,
			"desc": "Success"
		},
		"data": user_to_update.to_dict()
	}
	return jsonify(response_data), 200

#@app.delete("/users")
#def delete_users():
#	pass




#
# main...
#

if __name__ == "__main__":
 	app.run(host="127.0.0.1", port=5000, debug=True)
