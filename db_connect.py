import pymongo as py

url = 'mongodb://localhost:27017'
client = py.MongoClient(url)
db = client['mm_demo']