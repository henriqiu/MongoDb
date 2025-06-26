from pymongo import MongoClient
from dotenv import dotenv_values

mongo_uri = "mongodb+srv://malta:291107ze@cluster0.3u6t1r3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_uri)

database = mongo_client['database_test']
test_collection = database['test_collection']

person ={ "name": "Lucca de Enzo", "age": 12}
test_collection.insert_one(person)

config = dotenv_values('.env')
mongo_uri = config['URI_MONGO_ATLAS']

mongo_client = MongoClient(mongo_uri)

