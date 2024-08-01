from pymongo import MongoClient

# Use this cluster
client = MongoClient("mongodb+srv://asamant:Spring2024@cluster0.oovet.mongodb.net/?retryWrites=true&w=majority")
db = client.Users
posts = db.HWSet3
# print(collection)
post = {"userid": "as",
        "password": "654sphW"
        }
post_id = posts.insert_one(post).inserted_id
print(post)
