from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#import sys
#sys.path.insert(0,'/lahacks-safeLA/ML-models')
from safeLA_predict import predictSafeLA
#from ML-models/safeLA_predict.py import predictSafeLA
#from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class safeLA(Resource):
    def get(self,x,y):
       	result = predictSafeLA(x,y)
        max = 0
        for i in range(10):
            if (result[i]>result[max]):
                max = i
        max = max+1
        return max

api.add_resource(safeLA, '/safeLA')

if __name__ == '__main__':
    app.run(port="5002")
