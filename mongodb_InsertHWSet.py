from pymongo import MongoClient

# Use this cluster
client = MongoClient("mongodb+srv://asamant:Bhai0226@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")
db = client.HardwareSetApad
posts = db.HWSet1
# print(collection)
post = {"Description": "Hardware Set 3",
        "Capacity": "200",
        "Availability": "200",
        }
post_id = posts.insert_one(post).inserted_id
print(post)
