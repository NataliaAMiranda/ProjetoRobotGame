  #!/usr/bin/pythonfrom 
from flask import Flask, jsonify 
from flask import abort
from flask import make_response 
from flask_cors import CORS, cross_origin
from flask import request 
from flask import url_for
from flask_httpauth import HTTPBasicAuth
import pika
import sys
import json

auth = HTTPBasicAuth()

app = Flask(__name__)
CORS(app)

flags = [
          {
          'id'     : 1,
          'pausa'  : 0,
          'modo'   : 0,
          'inicio' : 0,
          'cacas'  : ""
          },
]
@app.route('/flags', methods=['GET'])
def obtem_flags():
		return jsonify({'flags' : flags})

@app.route('/flagpausa', methods=['GET'])
def obtem_flagpausa():
		resultado = [resultado for resultado in flags if resultado['id'] == 1]
		varpausa = resultado[0]['pausa']
		return jsonify({'pausa' : varpausa})

def atualiza_pausa(string_body):
		resultado = [resultado for resultado in flags if resultado['id'] == 1]
		resultado[0]['pausa'] = (string_body)
		return 0

def atualiza_modo(string_body):
		resultado = [resultado for resultado in flags if resultado['id'] == 1]
		resultado[0]['modo'] = int(string_body)
		return 0

def atualiza_inicio(string_body):
		resultado = [resultado for resultado in flags if resultado['id'] == 1]
		resultado[0]['inicio'] = int(string_body)
		return 0

def atualiza_cacas(string_body):
		resultado = [resultado for resultado in flags if resultado['id'] == 1]
		resultado[0]['cacas'] = string_body
		return 0

@app.route('/ler_pausa', methods=['GET'])
def ler_pausa():
		#credentials = pika.PlainCredentials('the_user', 'the_pass')
		credentials = pika.PlainCredentials('guest', 'guest')
		connection = pika.BlockingConnection(pika.ConnectionParameters(
                                                        host='localhost',
                                                        port=5672,
                                                        virtual_host='/',
                                                        credentials=credentials))
		channel = connection.channel()
		channel.exchange_declare(exchange='logs', exchange_type='fanout')
		result = channel.queue_declare(exclusive=True)
		queue_name = result.method.queue
		channel.queue_bind(exchange='logs', queue=queue_name)
		print('[*] Waiting for logs. To exit press CTRL+C')
		def callback(ch, method, properties, body):
				print(" [x] %r" % body)
				string_body = body.decode()				
				atualiza_pausa(string_body)
						
		channel.basic_consume(callback,queue=queue_name, no_ack=True)
		channel.start_consuming()
		return jsonify({'ok': '1'}), 200

@app.route('/ler_cadastro', methods=['GET'])
def ler_cadastro():
		#credentials = pika.PlainCredentials('the_user', 'the_pass')
		credentials = pika.PlainCredentials('guest', 'guest')
		connection = pika.BlockingConnection(pika.ConnectionParameters(
                                                        host='localhost',
                                                        port=5672,
                                                        virtual_host='/',
                                                        credentials=credentials))
		channel = connection.channel()
		channel.exchange_declare(exchange='logs', exchange_type='fanout')
		result = channel.queue_declare(exclusive=True)
		queue_name = result.method.queue
		channel.queue_bind(exchange='logs', queue=queue_name)
		print('[*] Waiting for logs. To exit press CTRL+C')
		def callback(ch, method, properties, body):
				print(type(body))
				print(" [x] %r" % body)
				string_body = body.decode()
				dado = json.loads(string_body)
				atualiza_modo(dado[0])
				atualiza_inicio(dado[1])
				atualiza_cacas(dado[2])
		channel.basic_consume(callback,queue=queue_name, no_ack=True)
		channel.start_consuming()
		return jsonify({'ok': '1'}), 200

if __name__ == "__main__":
    print('Servidor no ar!')
    
    app.run(host='0.0.0.0',port='5030', debug=True)
