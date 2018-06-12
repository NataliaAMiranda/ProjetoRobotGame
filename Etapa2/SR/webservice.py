#!/usr/bin/pythonfrom
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask_cors import CORS, cross_origin
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth
from manual import *

auth = HTTPBasicAuth()

app = Flask(__name__)
CORS(app)

oper = [
          {
          'id': 1,
          'dir' : 0,
          'steps' : 0,
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
    dire = request.json.get('dir', resultado[0]['dir'])
    steps = request.json.get('steps', resultado[0]['steps'])
    #mov = manual(dire,steps)
    #mov.movimento()
    print(steps)
    print(dire)
    return jsonify({'ok': '1'}), 201

if __name__ == "__main__":
    print('Servidor no ar!')
    app.run(host='0.0.0.0', port='5040', debug=True)
