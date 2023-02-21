#Code Adhyayana
import pymongo

client = pymongo.MongoClient("mongodb+srv://demo_user1:zOvcKXbZm732qUGy@cluster0.snjdnfh.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db.friends.insert_one({"Name": "Miss P",
                        "Address": {
                            "Address Line 1":"Beauty Palace",
                            "Room No": 420,
                            "Street": "Love Street",
                            "Zip Code": 143143
                        }
                        })

db.friends.insert_one({"Name": "Robin",
                        "Skills":[
                            "Python",
                            "Pyspark",
                            "SQL"
                        ]})

print("data has been added to collection")