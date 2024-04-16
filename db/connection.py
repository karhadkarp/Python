import pymongo
from pymongo import MongoClient
from pymongo import collection

cluster = MongoClient(
    'mongodb+srv://dilsedigital007:wh1teMayur@cluster0.opahplu.mongodb.net/Mongodb?retryWrites=true&w=majority')

db = cluster["sldb"]
collection = db["employee"]
post = {"name": "amar", "email": "amar@mail.com"}

collection.insert_one(post)
