from pymongo import MongoClient

# Use this cluster
client = MongoClient("mongodb+srv://asamant:Spring2024@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")
db = client.HardwareSet
posts = db.HWSet3
# print(collection)
post = {"Description": "This is HWSet3",
        "Capacity": 200,
        "Availability": 100
        }
post_id = posts.insert_one(post).inserted_id
print(post)
