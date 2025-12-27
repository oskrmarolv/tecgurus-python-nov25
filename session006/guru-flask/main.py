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


app = Flask(__name__)       # instancia principal de la aplicacion

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

USERS = [
	{ "id":"10001", "name":"Oscar" },
	{ "id":"10002", "name":"Gabriel" },
	{ "id":"10003", "name":"Maya" },
	{ "id":"10004", "name":"Jonathan" }
]

#@app.post("/users")
#def create_users():
#	pass

@app.get("/users")
def read_users():
	# Objeto respuesta
	response_data = {
		# cual es el status del proceso interno
		"status": {
			"code": "0x100",
			"desc": "Incomplete"
		},
		# payload interno del proceso
		"data": USERS
	}

	return jsonify(response_data), 200

#@app.put("/users")
#def update_users():
#	pass

#@app.delete("/users")
#def delete_users():
#	pass




#
# main...
#

if __name__ == "__main__":
 	app.run(host="127.0.0.1", port=5000, debug=True)
