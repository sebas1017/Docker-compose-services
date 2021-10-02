from faker import Faker
import itertools
from flask import Flask
from sqlalchemy import create_engine
import json
import sys
app =  Flask(__name__)
fake = Faker()


def random_data():
	insert_queries = []
	profiles = [dict(itertools.islice(fake.profile().items(), 6))  for data in range(13)]
	for profile in profiles:
		sql =""
		for llave, valor in list(profile.items()):
			if llave == 'current_location':
				coordinates = [str(coordinate) for coordinate in valor]
				profile.update(current_location =json.dumps({"coordinates":coordinates}))
		values = (str(list(profile.values())).replace("\\","")[1:-1])
		sql =f""" INSERT INTO profile (job, 
									 company, ssn, 
									 residence, current_location, 
									 blood_group)
			   VALUES ({values});""".replace("\n","")
		insert_queries.append(sql)
	return insert_queries

def execute_queries(list_queries_string=[], querie_type=''):
	db_name = 'rainbow_database'
	db_user = 'unicorn_user'
	db_pass = 'magical_password'
	db_host = 'database-service' # este es el servicio database declarado en el docker-compose
	db_port = '5432'
	# conexion a la base de datos POSTGRESQL
	try:
		db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
		db = create_engine(db_string)
		if querie_type == 'INSERT':
			for querie in list_queries_string:
				db.execute(querie).rowcount
		if querie_type == 'SELECT':
			for querie in list_queries_string:
				data_profiles = db.execute(querie).fetchall()
			return json.dumps( [dict(ix) for ix in data_profiles] ) #CREATE JSON
		if querie_type == 'DELETE':
			for querie in list_queries_string:
				data_profiles = db.execute(querie)
		return {"message":"proceso correcto"}
	except Exception as e:
		print("error en conexion con la base de datos", e)
		return {"status":"error en conexion con la base de datos"}


@app.route('/crear_registros')
def create_profiles():
	try:
		execute_queries(random_data(),"INSERT")
		return {"message":"proceso realizado correctamente"}
	except Exception:
		return {"message":"error en proceso de creacion de datos en faker-service"}

@app.route('/obtener_registros')
def get_profiles():
	querie_data= 'SELECT * FROM profile;'
	try:
		data_profiles = json.loads(
			execute_queries([querie_data],"SELECT"))
		return json.dumps(data_profiles)
	except Exception:
		return {"message":"error en consulta de datos en servicio faker-service"}

@app.route('/borrar_registros')
def delete_profiles():
	querie_data= 'DELETE FROM profile;'
	try:
		data_profiles =  execute_queries([querie_data],"DELETE")
		return json.dumps(data_profiles)
	except Exception:
		return {"message":"error en eliminacion de datos en servicio faker-service"}

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)
