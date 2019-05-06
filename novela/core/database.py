from flask import current_app
from pymongo import MongoClient

client = MongoClient(current_app.config['DB_CONNECTION'])
db = client.Emancipada


def find_by_id(query):
	return db.sujetos.find_one({
		'$or': [
			{'@id': query}, 
			{'rdfs:label': query},
			{'rdfs:type': query},
			{'ns1:producer': query},
			{'foaf:Person' :query}
		]
	})


def close_db(exception=None):
    client.close()
