#Code Adhyayana
import pymongo

client = pymongo.MongoClient("mongodb+srv://demo_user1:zOvcKXbZm732qUGy@cluster0.snjdnfh.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db.friends.insert_one({"Name": "Ishu"})

db.friends.insert_many([{"Name": "Ross"},
                        {"Name": "Joey"},
                        {"Name": "Jyoti"},
                        {"Name": "Monica"}])

print("data has been added to collection")