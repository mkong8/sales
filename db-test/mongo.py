from pymongo import MongoClient

HOST = 'localhost'
PORT = 27017

client = MongoClient(HOST, PORT)
db = client.examples

inventory = db.inventory

print(inventory.find_one())