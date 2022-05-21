database = {} #um dicionário, que tem a chave interesses para o controle
#dos interesses (que pessoa se interessa por que outra), e pessoas para o controle de pessoas (quem sao as pessoas e quais sao os dados pessoais de cada pessoa no sistema)
#voce pode controlar as pessoas de outra forma se quiser, nao precisa mudar nada
#do seu código para usar essa váriavel
database['interesses'] = { 
    100: [101, 20,3],
    200: [100,29],
    3: [100,34],
    9: []
}
database['PESSOA'] = [
        {
            "id": 9, 
            "nome": "maximus"
        }, 
        {
            "id": 3, 
            "nome": "aurelia"
        }
] #esse voce só faz se quiser guardar nessa lista os dicionários das pessoas

def todas_as_pessoas():
    return database['PESSOA']

def adiciona_pessoa(dic_pessoa):
    id = dic_pessoa['id']
    database['interesses'][id] = []
    database['PESSOA'].append(dic_pessoa)

class NotFoundError(Exception):
    pass

class IncompatibleError(Exception):
    pass

def localiza_pessoa(id_pessoa):
    for pessoa in database['PESSOA']:
        if pessoa['id'] == id_pessoa:
            return pessoa
    raise NotFoundError

def reseta():
    database['PESSOA'] = []
    database['interesses'] = {}

database['interesses'] = { 
    100: [101, 102, 103],
    200: [100],
    15: []
}

def adiciona_interesse(id_interessado, id_alvo_de_interesse): #200, 15
    pessoa1 = localiza_pessoa(id_interessado)
    pessoa2 = localiza_pessoa(id_alvo_de_interesse)
    try:
        if pessoa1['buscando'] not in pessoa2['sexo']:
            raise IncompatibleError
        else:
            database['interesses'][id_interessado].append(id_alvo_de_interesse)    
    except:
        database['interesses'][id_interessado].append(id_alvo_de_interesse)

def consulta_interesses(id_interessado):
    localiza_pessoa(id_interessado)
    return database['interesses'][id_interessado]

#essa funcao só vai ser testada
#quando estivermos fazendo matches
def remove_interesse(id_interessado,id_alvo_de_interesse):
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    if id_alvo_de_interesse in database['interesses'][id_interessado]:
        database['interesses'][id_interessado].remove(id_alvo_de_interesse)


def verifica_match(id1, id2):
    interesses1 = consulta_interesses(id1)
    interesses2 = consulta_interesses(id2)
    dois_deu_like_em_1 = id1 in interesses2
    um_deu_like_em_2 = id2 in interesses1
    return dois_deu_like_em_1 and um_deu_like_em_2
      
def lista_matches(id_pessoa):
    lista = []
    interesses_pessoa = consulta_interesses(id_pessoa)
    for pessoa in interesses_pessoa:
        if verifica_match(id_pessoa, pessoa):
            lista.append(pessoa)
    return lista

