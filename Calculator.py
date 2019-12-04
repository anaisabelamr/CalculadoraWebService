#from sumTwoNumbers import *
#from substractTwoNumbers import *
#from multiplyTwoNumbers import *
#from divideTwoNumbers import *

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def __init__(self, a, b):
	self.a = 1
	self.b = 2

def soma(self):
	return self.a + self.b

def subtrai(self):
	return self.a - self.b

def multiplica(self):
	return self.a * self.b

def divide(self):
	return self.a / self.b

@app.route('/welcome')
def api_welcome():
	return 'Laboratório de Sistemas Distribuídos - 2019.4 - UFPA'

@app.route('/soma', methods = ['GET', 'POST'])
def api_addition():
	content = request.get_json()
	print("A soma é: ".format(soma))
	#return str(soma)

@app.route('/mult', methods = ['GET', 'POST'])
def api_multiplication():
	content = request.get_json()  
	return str(multiplica)

@app.route('/div', methods = ['GET', 'POST'])
def api_division():
	content = request.get_json()
	return str(divide)

@app.route('/sub', methods = ['GET', 'POST'])
def api_substraction():
	content = request.get_json()
	return str(subtrai)

if __name__ == '__main__':
	app.run(debug=True)
	#host='127.0.0.1:5000
