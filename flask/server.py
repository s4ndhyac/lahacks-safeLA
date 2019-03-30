from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
#import sys
#sys.path.insert(0,'/lahacks-safeLA/ML-models')
from safeLA_predict import predictSafeLA
#from ML-models/safeLA_predict.py import predictSafeLA
#from flask.ext.jsonpify import jsonify
import numpy as np

app = Flask(__name__)
api = Api(app)

@app.route('/safeLA/')
def getSafeLAScore():
  x = request.args.get('x')
  y = request.args.get('y')
  result = predictSafeLA(x, y)
  argmax = np.argmax(result)
  label_dict = {pos: letter
                for pos, letter in enumerate(range(0,10))}
  max = label_dict[argmax] + 1
  return str(max)


if __name__ == '__main__':
  app.run(debug=True, port="5002")
