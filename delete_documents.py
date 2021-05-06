from pymongo import MongoClient 
cliente = MongoClient('mongodb://admin:mongoadmin@localhost:27017')
db = cliente['test']
colecao = db['portaismotos']
colecao.delete_many({})
cliente.close()
