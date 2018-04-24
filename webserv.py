#!/usr/bin/python
#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask_cors import CORS, cross_origin
from flask import make_response
from flask import request
from flask import url_for
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

oper = [
          {
	  'id': 1,
          'dir' : 1,
          'steps' : 1
	  #'novojogo': True,
	  #'novajogada': True
          },
]

@app.route('/oper', methods=['GET'])
def obtem_oper():
    return jsonify({'oper': oper})

@app.route('/atualiza', methods=['PUT'])
def atualizar_valores():
    resultado = [resultado for resultado in oper if resultado['id'] == 1]
    resultado[0]['dir'] = request.json.get('dir', resultado[0]['dir'])
    resultado[0]['steps'] = request.json.get('steps', resultado[0]['steps'])
    print "atualizou"
    return jsonify({'ok': '1'}), 201
if __name__ == "__main__":
    print "Servidor no ar!"
    app.run(host='0.0.0.0', debug=True)


