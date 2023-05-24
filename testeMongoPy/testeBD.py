from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['banco_teste']

colecao = db['mongo_flask']

# Adicionar registros

dados = [
    {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'},
    {'nome': 'Maria', 'idade': 30, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Pedro', 'idade': 28, 'cidade': 'Belo Horizonte'}
]

# resultado = colecao.insert_many(dados)

# print('Foram inseridos', resultado.inserted_ids, 'documentos')

# Fazer update de registro

filtro = {'idade': 30}

update = {'$set': {'nome': 'Maria Josefina'}}

result = colecao.update_many(filtro, update)

print('Número de documentos atualizados:', result.modified_count)

# Fazer delete de um registro

filtro2 = {'nome': 'Maria Josefina'}

resultDelete = colecao.delete_many(filtro2)

print(resultDelete.deleted_count)

# Listar as coleções

coleecoess = db.list_collection_names()

print(coleecoess)
