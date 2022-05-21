from flask import Flask, jsonify, request
import estrutura_interesses as i

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/pessoas')
def listar_pessoas():
    return jsonify(i.todas_as_pessoas())

@app.route('/pessoas', methods=['POST'])
def criar_pessoas():
    dict_pessoa = request.json
    i.adiciona_pessoa(dict_pessoa)
    return jsonify(i.todas_as_pessoas())

@app.route('/pessoas/<int:id_pessoa>')
def procura_pessoa(id_pessoa):
    return jsonify(i.localiza_pessoa(id_pessoa))

@app.route('/reseta', methods=['POST'])
def reseta():
    return jsonify(i.reseta())

@app.route('/sinalizar_interesse/<int:id1>/<int:id2>', methods=['PUT'])
def sinalizar_interesse(id1, id2):
    try:
        i.adiciona_interesse(id1, id2)
        return jsonify(i.todas_as_pessoas())
    except:
        return {'Erro': 'Uma das pessoas não existe.'}, 404

@app.route('/sinalizar_interesse/<int:id1>/<int:id2>', methods=['DELETE'])
def remover_interesse(id1, id2):
    try:
        i.remove_interesse(id1, id2)
        return jsonify(i.todas_as_pessoas())
    except:
        return {'Erro': 'Uma das pessoas não existe.'}, 404

@app.route('/interesses/<int:id_pessoa>')
def lista_interessses(id_pessoa):
    return jsonify(i.consulta_interesses(id_pessoa))

@app.route('/matches/<int:id_pessoa>')
def lista_matches(id_pessoa):
    try:
        return jsonify(i.lista_matches(id_pessoa))
    except:
        return {'Erro': 'Uma das pessoas não existe.'}, 404




if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
    # host é o nome do servidor onde o flask vai ficar
    # port é a porta :P
    # debug: liga o auto-reload e outras coisas úteis pra debuggar,
    # PRECISA desligar se um dia for pra produção