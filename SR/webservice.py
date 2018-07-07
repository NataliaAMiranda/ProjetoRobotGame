 #!/usr/bin/pythonfrom
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


oper = [
          {
          'id': 1,
          'dir' : 0,
          'steps' : 0,
          'caca':[[1,2],[4,2],[6,7],[9,1],[2,3],[6,7],[9,1],[2,3]],
          },
]

@app.route('/oper', methods=['GET'])
def obtem_oper():
    return jsonify({'oper': oper})

@app.route('/atualiza', methods=['PUT'])
def atualizar_valores():
    resultado = [resultado for resultado in oper if resultado['id'] == 1]
    resultado[0]['dir'] = request.json    
    print("Alterou") .get('dir', resultado[0]['dir'])
    resultado[0]['steps'] = request.json.get('steps', resultado[0]['steps'])
    dire = request.json.get('dir', resultado[0]['dir'])
    steps = request.json.get('steps', resultado[0]['steps'])

    mov = manual(dire,steps)
    mov.movimento()

    print('atualizou')
    return jsonify({'ok': '1'}), 201
    
@app.route('/automatico', methods=['PUT'])
def automatico():
    resultado = [resultado for resultado in oper if resultado['id'] == 1]
    resultado[0]['caca'] = request.json.get('caca', resultado[0]['caca'])  

    return jsonify({'ok': '1'}), 201

if __name__ == "__main__":
    print('Servidor no ar!')
    app.run(host='0.0.0.0', port='5040', debug=True)

