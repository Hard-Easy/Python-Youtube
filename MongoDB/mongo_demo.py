#Code Adhyayana
import pymongo

client = pymongo.MongoClient("connection string with user name and password")
db = client.test

print(db.name)

db.my_collection.insert_one({"x": 10})
db.my_collection.insert_one({"x": 20})
db.my_collection.insert_one({"x": 30})

print("data has been added to collection")