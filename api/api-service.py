from flask import Flask
import requests
import json
import sys
app =  Flask(__name__)


@app.route("/")
def home():
	try:
		url = f"http://faker-service:{3000}/obtener_registros"
		res = requests.get(url).json()
		return json.dumps(res)
	except Exception as e:
		print(e, file=sys.stderr) #salida atraves de los logs
		return {"message":"error en consulta de datos"}
   

@app.route("/admin/borrar_registros")
def delete_records():
	url = f"http://faker-service:{3000}/borrar_registros"
	res = requests.get(url).json()
	return json.dumps(res)

@app.route("/admin/crear_registros")
def create_records():
	url = f"http://faker-service:{3000}/crear_registros"
	res = requests.get(url).json()
	return json.dumps(res)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=81, debug=True)