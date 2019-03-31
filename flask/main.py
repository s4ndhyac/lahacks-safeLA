from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
#import sys
#sys.path.insert(0,'/lahacks-safeLA/ML-models')
from safeLA_predict import predictSafeLA
from LArent_predict import predictRentLA
#from flask.ext.jsonpify import jsonify
import numpy as np

from keras import backend as K

app = Flask(__name__)
api = Api(app)

@app.route('/safeLA/')
def getSafeLAScore():
  K.clear_session()
  x = request.args.get('x')
  y = request.args.get('y')
  result = predictSafeLA(x, y)
  argmax = np.argmax(result)
  label_dict = {pos: letter
                for pos, letter in enumerate(range(0,10))}
  max = label_dict[argmax] + 1
  return str(max)

@app.route('/rentLA/')
def getRent():
  K.clear_session()
  x = request.args.get('x')
  y = request.args.get('y')
  result = predictRentLA(x, y)
  rentavg = np.array2string(result, precision=3, separator="")
  return rentavg

@app.route('/test/')
def getTest():
  return "Hello World"

if __name__ == '__main__':
  app.run()
