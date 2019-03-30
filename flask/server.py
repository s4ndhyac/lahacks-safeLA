
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class safeLA(Resource):
	def get(self,x,y):
		result = {'message': 'hello world'}
		return "Hello World"

api.add_resource(safeLA, '/safeLA')

if __name__ == '__main__':
	app.run(port="5002")
