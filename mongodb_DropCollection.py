from pymongo import MongoClient
import datetime

#Use this cluster
client = MongoClient("mongodb+srv://asamant:EE461LSp22@cluster0.oovet.mongodb.net/HWSet1?retryWrites=true&w=majority")
db = client.HWSet1
posts = db.HWSet1
#print(collection)
post = {"Description": "Hardware Set 3",
        "Capacity": "200",
        "Availability": "200",
       }
post_id = posts.insert_one(post).inserted_id
print(post)