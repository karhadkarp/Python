import pymongo
from pymongo import MongoClient
from pymongo import collection

cluster = MongoClient(
    'mongodb+srv://admin:admin123@cluster0.fbsul.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["sldb"]
collection = db["employee"]
post = {"name": "amar", "email": "amar@mail.com"}

collection.insert_one(post)
