import pymongo
from pymongo import MongoClient
from pymongo import collection


def getDBConnection(username, password, database):
    cluster = MongoClient(
        'mongodb+srv://' + username + ':' + password + '@cluster0.opahplu.mongodb.net/' + database + '?retryWrites=true&w=majority')

    #    cluster = MongoClient(
    #        'mongodb+srv://dilsedigital007:wh1teMayur@cluster0.opahplu.mongodb.net/Mongodb?retryWrites=true&w=majority')

    db = cluster["RMApp"]
    return db

def getProducts(database):
    
    collection = database["ProductData"]
    collection.find_one()

def addProducts(products, database):
    collection = database["ProductData"]
    post = {"name": "amar", "email": "amar@mail.com"}

    collection.insert_one(post)
    
getDBConnection('dilsedigital007', 'wh1teMayur', 'Mongodb')
